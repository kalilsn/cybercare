angular.
    module("customer").
    factory("Customer", ["$resource",
        function($resource) {
            return $resource("customers/:id", {id:"@id"}, {
                'update': {
                    method:'PUT',
                    transformResponse: angular.noop
                },
                'save': {
                    method:'Post',
                    transformResponse: angular.noop
                }
            });
        }
    ]); 