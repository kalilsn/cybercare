angular.
    module("cybercare").
    component("customerList", {
        templateUrl: "templates/customer-list.template.html",
        controller: ["Customer", "$mdToast", "$mdDialog", "$scope",
            function CustomerListController(Customer, $mdToast, $mdDialog, $scope) {
                var api = new Customer();
                $scope.customers = Customer.query();
                $scope.edit = function(e, i) {
                    $mdDialog.show({
                        templateUrl: "templates/edit-customer.template.html",
                        locals: {i: i},
                        scope: $scope.$new(),
                        preserveScope: true,
                        controller: EditCustomerController,
                        controllerAs: "ctrl",
                        targetevent: e
                    });
                };
                $scope.removeCustomer = function(customer, i) {
                    name = customer.name;
                    console.log(customer);
                    customer.$remove(function() {
                        $scope.customers.splice(i, 1);
                        $mdToast.showSimple("Removed " + name + " from the database.");
                    });
                };
            }
        ]
    }
);

function EditCustomerController(Customer, $mdToast, $mdDialog, $scope, i) {
    var self = this;
    self.customer = $scope.customers[i];
    self.USstates = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'];
    self.update = function() {
        console.log(self.customer);
        self.customer.$update(function() {
            $mdToast.showSimple("Updated " + self.customer.name + " in the database.");
            self.close();
        });
    };
    self.close = function() {
        $mdDialog.hide();
    };
}

