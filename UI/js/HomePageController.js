angular.module('homePageApp', ['userDataModelApp'])
.controller('HomePageController', function HomePageController($scope, $http, userDataModel) {

	vm = $scope;
	vm.myShares = userDataModel.myShares;
	vm.allShares = userDataModel.allShares;
	vm.commonMap = userDataModel.commonMap;
	var url = userDataModel.properties.url;
	
	function getLastUpdatedDate(){
		var data = {
		'command' : "getLastUpdatedDate",
		'argumentsList' : []
		}
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http({
			url: url,
			method: "POST",
			data: JSON.stringify(data)
		})
		.then(function(response) {
			vm.commonMap.lastUpdatedDate = response.data['success'];
			console.log(response.data['success']);
			hidePreloader();
		});
	}
	
	if(vm.commonMap.lastUpdatedDate == "")
		getLastUpdatedDate();
	
	vm.dailyUpdate = function(){
		showPreloader();
		var date = new Date(vm.commonMap.lastUpdatedDate);
		var yyyy = date.getFullYear();
		var mm = date.getMonth() < 9 ? "0" + (date.getMonth() + 1) : (date.getMonth() + 1);
		var dd  = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
		
		var date = dd + '/' + mm + '/' + yyyy;
		var data = {
		'command' : "dailyUpdate",
		'argumentsList' : [date]
		}
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http({
			url: url,
			method: "POST",
			data: JSON.stringify(data)
		})
		.then(function(response) {
			console.log(response.data['success']);
			getLastUpdatedDate();
		});
	}
	
	vm.removeDuplicates = function(){
		showPreloader();
		var data = {
		'command' : "removeDuplicates",
		'argumentsList' : []
		}
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http({
			url: url,
			method: "POST",
			data: JSON.stringify(data)
		})
		.then(function(response) {
			console.log(response.data['success']);
			hidePreloader();
		});
	}
	
	vm.sortData = function(){
		showPreloader();
		var data = {
		'command' : "sortData",
		'argumentsList' : []
		}
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http({
			url: url,
			method: "POST",
			data: JSON.stringify(data)
		})
		.then(function(response) {
			console.log(response.data['success']);
			hidePreloader();
		});
	}
	
});