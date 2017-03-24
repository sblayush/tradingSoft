angular.module('userDataModelApp', [])
.factory('userDataModel', function($http) {
	var myShares = [];
	var allShares = [];
	var properties = {
		EMArange : 14,
		SMArange : 21,
		datesRange : 100
	}
	var url = "http://localhost:8888/runCommand";
	
	var commonMap = {
		selectedShare : "none",
		indicators : {},
		lastUpdatedDate : ""
	}
	
	
	$http.get('propertiesFile.properties').then(function (response) {
		angular.forEach(response.data, function(propertyValue, propertyType) {
			properties[propertyType] = propertyValue;
		});
	});
	
	return {
		myShares : myShares,
		allShares : allShares,
		commonMap : commonMap,
		properties : properties
	}
});