angular.
    module("cybercare").
    component("customerList", {
        templateUrl: "templates/customer-list.template.html",
        controller: ["Customer", "$mdToast",
            function CustomerListController(Customer, $mdToast) {
                var self = this;
                var api = new Customer();
                self.customers = Customer.query();
                self.removeCustomer = function(customer, i) {
                    api.$remove({id: customer.id}, function() {
                        self.customers.splice(i, 1);
                        $mdToast.showSimple("Removed " + customer.name + " from the database.");
                    });
                };
            }
        ]
    });
