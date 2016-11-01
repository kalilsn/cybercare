from bottle import route, request, Bottle, run, response, HTTPError, HTTPResponse, hook, static_file
from bottle.ext import sqlite
from collections import OrderedDict
import json
import sqlite3

# Bottle initialization and database setup
dbfilename = "cybercare.db"
app = application = Bottle()

plugin = sqlite.Plugin(dbfile=dbfilename, keyword="db")
app.install(plugin)


# Enable cors and set format to json
@hook('after_request')
def set_headers():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers["Content-Type"] = "application/json"


# Returns a formatted dictionary from an SQLite cursor object
# Assumes a query has been executed already
def to_json(cursor):
    # Unflatten address from its sql representation
    def nest_address(d):
        address = {}
        for key in ["street", "city", "state", "zip"]:
            address[key] = d.pop(key)
        d["address"] = address
        return d

    keys = [x[0] for x in cursor.description]
    result = cursor.fetchall()

    if len(result) == 1:
        row = nest_address(OrderedDict(zip(keys, result[0])))
        return row
    else:
        rows = [nest_address(OrderedDict(zip(keys, r))) for r in result]
        print len(result)
        return rows


def json_error(e, s):
    return dict(body=e, status=s)


@route('/customers/', method="GET", apply=[plugin])
@route('/customers', method="GET", apply=[plugin])
def list_customers(db):
    try:
        cursor = db.execute('SELECT * FROM customers')
        customers = to_json(cursor)
        if customers:
            return json.dumps(customers)
        else:
            response.status = 500
            return json_error("Database appears to be empty.", 500)
    except sqlite3.Error as e:
        response.status = 500
        return json_error(e.args[0], 500)


# Sample return: {"id": 2, "name": "Alma Jensen", "email": "ep@wiwi.com", "telephone": 481190297, "address": {"city": "Ucimhug", "state": "UT", "street": "314 Conu Manor", "zip": "39067"}}
# Will always have the same order
@route('/customers/<id:int>', method="GET", apply=[plugin])
def get_customer(id, db):
    try:
        cursor = db.execute('SELECT * FROM customers WHERE id = ?', (str(id),))
        customer = to_json(cursor)
        if customer:
            return json.dumps(customer)
        else:
            response.status = 404
            return json_error("No customer found by that id.", 404)
    except sqlite3.Error as e:
        response.status = 500
        return json_error(e.args[0], 500)


def flatten_address(d):
    address = d.pop("address")
    for k, v in address.items():
        d[k] = v

    return d


# Sample request: {"name": "Alma Jensen", "email": "ep@wiwi.com", "telephone": 481190297, "address": {"city": "Ucimhug", "state": "UT", "street": "314 Conu Manor", "zip": "39067"}}
@route('/customers/', method="POST", apply=[plugin])
@route('/customers', method="POST", apply=[plugin])
def add_customer(db):

    def format_customer(data):
        flatten_address(data)
        # Order the data
        keys = ["name", "email", "telephone", "street", "city", "state", "zip"]
        customer = []
        try:
            for key in keys:
                customer.append(data[key])
        except KeyError:
            raise ValueError("%s is required." % key)
        return customer

    try:
        customer = format_customer(request.json)
        cursor = db.execute("INSERT INTO customers(name,email,telephone,street,city,state,zip) VALUES (?,?,?,?,?,?,?)", customer)

        id = cursor.lastrowid
        cursor = db.execute('SELECT * FROM customers WHERE id = ?', (str(id),))
        customer = to_json(cursor)
        return json.dumps(customer)

    except sqlite3.Error as e:
        response.status = 500
        return json_error(e.args[0], 500)
    except ValueError as e:
        response.status = 400
        return json_error(e.args[0], 400)


@route('/customers/<id:int>', method="PUT", apply=[plugin])
def update_customer(id, db):

    def validate(data):
        return

    try:
        print request.json

        result = db.execute("SELECT * FROM customers WHERE id = ?", (str(id),))
        customer = result.fetchone()
        if not customer:
            raise KeyError(request.json["name"])

        updates_dict = flatten_address(request.json)

        updates = ', '.join(['{} = "{}"'.format(k, v) for k, v in updates_dict.items()])

        update = db.execute("UPDATE customers SET %s WHERE id = ?" % updates, (str(id),))

        cursor = db.execute('SELECT * FROM customers WHERE id = ?', (str(id),))
        customer = to_json(cursor)
        return json.dumps(customer)


    except KeyError as e:
        response.status = 400
        return json_error("Customer %s not found" % e.args[0], 400)

    except sqlite3.Error as e:
        response.status = 500
        return json_error(e.args[0], 400)


@route('/customers/<id:int>', method="DELETE", apply=[plugin])
def delete_customer(id, db):
    try:
        result = db.execute("SELECT * FROM customers WHERE id = ?", (str(id),))
        customer = result.fetchone()
        if not customer:
            raise KeyError(customer["name"])

        db.execute("DELETE FROM customers WHERE id = ?", (str(id),))
        return HTTPResponse(body="Deleted %s from the database." % customer["name"], status=200)

    except KeyError as e:
        response.status = 400
        return json_error("Customer %s not found" % e.args[0], 500)

    except sqlite3.Error as e:
        response.status = 500
        return json_error(e.args[0], 500)


@route('/')
@route('')
def index():
    return static_file("index.html", "./")


# Serve static files
@route('/<file:path>')
def static(file):
    return static_file(file, "./")


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
