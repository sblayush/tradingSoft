angular.module("tradingSoftApp", ["ngRoute", "homePageApp", "myPortfolioApp", "viewStockApp", "propertiesPageApp"])
.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "home.html",
        controller : "HomePageController"
    })
	.when("/home", {
        templateUrl : "home.html",
        controller : "HomePageController"
    })
    .when("/myPortfolio", {
        templateUrl : "myPortfolio.html",
        controller : "MyPortfolioController"
    })
	.when("/allStocksList", {
        template : "<h1>Banana</h1><p>Bananas contain around 75% water.</p>"
    })
    .when("/viewStock", {
        controller : "ViewStockController",
        templateUrl : "viewStock.html"
    })
	.when("/propertiesPage", {
        controller : "PropertiesPageController",
        templateUrl : "propertiesPage.html"
    });
});