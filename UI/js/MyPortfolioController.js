angular.module('myPortfolioApp', ['userDataModelApp'])
.controller('MyPortfolioController', function MyPortfolioController($scope, $http, userDataModel) {

	vm = $scope;
	vm.myShares = userDataModel.myShares;
	vm.allShares = userDataModel.allShares;
	vm.commonMap = userDataModel.commonMap;
	var url = userDataModel.properties.url;
	
	if(vm.allShares.length == 0){
		(function(){
			var data = {
				'command' : "getAllSharesList",
				'argumentsList' : []
				}
			$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
			$http({
				url: url,
				method: "POST",
				data: JSON.stringify(data)
			})
			.then(function(response) {
				console.log(response.data)
				userDataModel.allShares = response.data['success'];
				vm.allShares = userDataModel.allShares;
			});
		}());
		
		(function(){
			var data = {
				'command' : "getMyPortfolioSharesList",
				'argumentsList' : []
				}
			$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
			$http({
				url: url,
				method: "POST",
				data: JSON.stringify(data)
			})
			.then(function(response) {
				console.log(response.data)
				userDataModel.myShares = response.data['success'];
				vm.myShares = userDataModel.myShares;
			});
		}());
	}
	
	vm.removeRow = function (idx) {
		vm.myShares.splice(idx, 1);
	};
	
	vm.addShare = function(name){
		if(vm.myShares.indexOf(name) === -1){
			vm.myShares.push(name);
			vm.myShares.sort();
		}
	}
	
	vm.saveMyPortfolioChanges = function(){
		showPreloader();
		var data = {
			'command' : "saveMyPortfolioChanges",
			'argumentsList' : [vm.myShares]
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