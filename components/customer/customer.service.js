angular.
    module("customer").
    factory("Customer", ["$resource",
        function($resource) {
            return $resource("customers/:id");
        }
    ]); 