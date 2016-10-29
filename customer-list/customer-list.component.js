angular.
    module("cybercare").
    component("customerList", {
        templateUrl: "customer-list/customer-list.template.html",
        controller: ["$http",
            function CustomerListController($http) {
                var self = this;
                $http.get('customers').then(function(response) {
                    self.customers = response.data.data;
                });

                self.remove = function remove(id) {
                    $http.delete('customers/' + id).then(function(response) {
                        
                    });
                };
            }
        ]
    });
