angular.module('propertiesPageApp', ['userDataModelApp'])
.controller('PropertiesPageController', function PropertiesPageController($scope, $http, userDataModel) {
	vm = $scope;
	vm.properties = userDataModel.properties;
	hidePreloader();
	var url = userDataModel.properties.url;
	
	vm.saveProperties = function(){
		showPreloader();
		var data = {
			'command' : "saveProperties",
			'argumentsList' : [JSON.stringify(vm.properties)]
			}
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http({
			url: url,
			method: "POST",
			data: JSON.stringify(data)
		})
		.then(function(response) {
			console.log(response.data);
			hidePreloader();
		});
	}
});