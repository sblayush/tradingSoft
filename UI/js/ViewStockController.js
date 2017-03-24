angular.module('viewStockApp', ['userDataModelApp'])
.controller('ViewStockController', function ViewStockController($scope, $http, userDataModel) {
	angular.element(document).ready(function () {
		plotEmptyGraph();
		createPageColorPicker();
	});
	
	vm = $scope;
	vm.myShares = userDataModel.myShares;
	vm.allShares = userDataModel.allShares;
	vm.commonMap = userDataModel.commonMap;
	vm.commonMap.selectedShare = "none";
	vm.indicators = userDataModel.commonMap['indicators'];
	vm.properties = userDataModel.properties;
	vm.overlayMap = {
		EMA: {'selected' : false, 'range' : vm.properties.EMArange},
		SMA: {'selected' : false, 'range' : vm.properties.SMArange}
	}
	
	var url = "http://localhost:8888/runCommand";
	var $chartDiv = $('#chart-container');
	var chart = anychart.stock();
	var plot = chart.plot(0);
	var table = anychart.data.table(0);
	var legend = plot.legend();
    var annotationsColor;
	var annotation = plot.annotations();
	
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
	
	vm.selectOverlay = function(overlayName){
		if(vm.overlayMap[overlayName].selected)
		{
			vm.overlayMap[overlayName].selected = false;
			plot.removeSeries(overlayName);
		}
		else
		{
			vm.overlayMap[overlayName].selected = true;
			switch(overlayName){
				case "EMA" :
					var overlayMapping = table.mapAs({'value': 4});
					var series = plot.ema(overlayMapping, vm.properties.EMArange).series();
					series.id(overlayName);
					break;
				case "SMA" :
					var overlayMapping = table.mapAs({'value': 4});
					var series = plot.sma(overlayMapping, vm.properties.SMArange).series();
					series.id(overlayName);
					break;
			}
		}
	}
	
	vm.getPoints = function(){
		showPreloader();
		var data = {
		'command' : "getPoints",
		'argumentsList' : []
		}
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http({
			url: url,
			method: "POST",
			data: JSON.stringify(data)
		})
		.then(function(response) {
			vm.indicators = response.data['success'];
			vm.commonMap['indicators'] = vm.indicators;
			console.log(response.data['success']);
			hidePreloader();
		});
	}
	
	vm.saveAnnotations = function(){
		showPreloader();
		var data = {
		'command' : "saveAnnotations",
		'argumentsList' : [vm.commonMap.selectedShare, JSON.stringify(annotation.toJson())]
		}
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http({
			url: url,
			method: "POST",
			data: JSON.stringify(data)
		})
		.then(function(response) {
			vm.indicators = response.data['success'];
			vm.commonMap['indicators'] = vm.indicators;
			console.log(response.data['success']);
			hidePreloader();
		});
	}
	
	if(Object.keys(vm.indicators).length == 0)
	{
		vm.getPoints();
	}
	
	vm.selectShare = function(shareName){
		showPreloader();
		vm.commonMap.selectedShare = shareName;
		var data = {
			'command' : "getStockData",
			'argumentsList' : [shareName]
			}
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http({
			url: url,
			method: "POST",
			data: JSON.stringify(data)
		})
		.then(function(response) {
			updateGraph(shareName, response.data['success']);
			//console.log(response.data['success'].slice((-1)*parseInt(vm.properties.datesRange)));
			hidePreloader();
		});
	}
	
	function updateGraph(stockName, data){
		table.remove();
		plot.removeAllSeries();
		table.addData(data['data'].slice((-1)*parseInt(vm.properties.datesRange)));
		var ohlcMapping = table.mapAs({'open': 1, 'high': 2, 'low': 3, 'close': 4});
		var scrollerMapping = table.mapAs({'value': 5});
		chart.scroller().area(scrollerMapping).color("#253992 0.3").stroke("#253992");
		
		var series = plot.candlestick(ohlcMapping).name(stockName);
		series.legendItem().iconType('risingfalling');
		
		annotation.fromJson(data['annotations']);
	}
	
	function plotEmptyGraph(){
		initTooltip('bottom');
		chart.padding(0, 30, 5, 5);
		
		plot.grid().enabled(true);
		plot.grid(1).enabled(true).layout('vertical');
		plot.minorGrid().enabled(true);
		plot.minorGrid(1).enabled(true).layout('vertical');
		
		chart.contextMenu().itemsFormatter(contextMenuItemsFormatter);
		chart.listen("annotationDrawingFinish", onAnnotationDrawingFinish);
		chart.listen("annotationSelect", onAnnotationSelect);
		chart.listen("annotationUnSelect", function () {
			$('.color-picker[data-color="fill"]').removeAttr('disabled');
			$('.select-marker-size').removeAttr('disabled');
			$('.drawing-tools-solo').find('.bootstrap-select').each(function () {
				$(this).removeClass('open');
			})
		});
		chart.listen('chartDraw', function () {
			hidePreloader();
		});
		chart.container("chart-container");
		chart.draw();
	}
	
	function createPageColorPicker() {
		var colorPicker = $('.color-picker');
		var strokeWidth;
		var STROKE_WIDTH = 1;
		colorPicker.colorpickerplus();
		colorPicker.on('changeColor', function (e, color) {
			var annotation = chart.annotations().getSelectedAnnotation();

			if (annotation) {
				switch ($(this).data('color')) {
					case 'fill' :
						annotation.fill(color);
						break;
					case 'stroke' :
						strokeWidth = annotation.stroke().thickness || STROKE_WIDTH;
						strokeDash = annotation.stroke().dash || '';
						var settings = {
							thickness: strokeWidth,
							color: color,
							dash: strokeDash
						};
						annotation.stroke(settings);
						annotation.hoverStroke(settings);
						annotation.selectStroke(settings);
				}
			}

			if (color == null) {
				$('.color-fill-icon', $(this)).addClass('colorpicker-color');
			} else {
				$('.color-fill-icon', $(this)).removeClass('colorpicker-color');
				$('.color-fill-icon', $(this)).css('background-color', color);
			}
		});
	}

	function removeSelectedAnnotation() {
		var annotation = chart.annotations().getSelectedAnnotation();
		if (annotation) chart.annotations().removeAnnotation(annotation);
		return !!annotation;
	}

	function removeAllAnnotation() {
		chart.annotations().removeAllAnnotations();
	}

	function onAnnotationDrawingFinish() {
		setToolbarButtonActive(null);
	}

	function onAnnotationSelect(evt) {
		var annotation = evt.annotation;
		var colorFill;
		var colorStroke;
		var strokeWidth;
		var strokeDash;
		var strokeType;
		var markerSize;
		var STROKE_WIDTH = 1;
		// val 6 in select = 'solid'
		var STROKE_TYPE = '6';
		var $strokeSettings = $('#select-stroke-settings');
		var $markerSize = $('#select-marker-size');
		var $markerSizeBtn = $('.select-marker-size');
		var $colorPickerFill = $('.color-picker[data-color="fill"]');
		var $colorPickerStroke = $('.color-picker[data-color="stroke"]');

		if (annotation.fill !== undefined) {
			$colorPickerFill.removeAttr('disabled');
			colorFill = annotation.fill();
		} else {
			$colorPickerFill.attr('disabled', 'disabled');
		}

		if (typeof annotation.stroke() === 'function') {
			colorStroke = $colorPickerStroke.find('.color-fill-icon').css('background-color');
			colorFill = $colorPickerFill.find('.color-fill-icon').css('background-color');

			if (colorFill.indexOf('a') === -1) {
				colorFill = colorFill.replace('rgb', 'rgba').replace(')', ', 0.5)');
			}

			if ($strokeSettings.val()) {
				switch ($strokeSettings.val()[0]) {
					case '6' :
					case '7' :
					case '8' :
						strokeType = $strokeSettings.val()[0];
						strokeWidth = $strokeSettings.val()[1] || STROKE_WIDTH;
						break;
					default :
						strokeWidth = $strokeSettings.val()[0];
						strokeType = $strokeSettings.val()[1];
						break;
				}
			} else {
				strokeWidth = STROKE_WIDTH;
				strokeType = STROKE_TYPE;
			}

		} else {
			colorStroke = annotation.stroke().color;
			strokeWidth = annotation.stroke().thickness;
			strokeDash = annotation.stroke().dash;
		}

		switch (strokeType) {
			case '6' :
				strokeType = null;
				break;
			case '7' :
				strokeType = '1 1';
				break;
			case '8' :
				strokeType = '10 5';
				break;
		}

		if (strokeType === undefined) {
			strokeType = strokeDash;
		}

		if (annotation.type === 'marker') {
			markerSize = annotation.size();

			if ($('.choose-marker').hasClass('open')) {
				$markerSize.val($markerSize.val()).selectpicker('refresh');
				annotation.size($markerSize.val());
				$markerSizeBtn.removeAttr('disabled')
			} else {
				$markerSize.removeAttr('disabled').val(markerSize).selectpicker('refresh');
				annotation.size(markerSize);
				$markerSizeBtn.removeAttr('disabled')
			}
			$markerSizeBtn.removeAttr('disabled');

		} else {
			$markerSizeBtn.attr('disabled', 'disabled');
		}

		var settings = {
			thickness: strokeWidth,
			color: colorStroke,
			dash: strokeType
		};

		annotation.stroke(settings);
		annotation.hoverStroke(settings);
		annotation.selectStroke(settings);

		if (annotation.fill !== undefined) {
			annotation.fill(colorFill);
		}

		switch (strokeType) {
			case '1 1' :
				strokeDash = 7;
				break;
			case '10 5' :
				strokeDash = 8;
				break;
			default :
				strokeDash = 6;
				break;
		}

		$colorPickerFill.find('.color-fill-icon').css('background-color', colorFill);
		$colorPickerStroke.find('.color-fill-icon').css('background-color', colorStroke);
		$strokeSettings.val([strokeWidth, strokeDash]).selectpicker('refresh');
	}

	function contextMenuItemsFormatter(items) {
		// insert context menu item on 0 position
		items.splice(0, 0, {
			text: "Remove selected annotation",
			action: removeSelectedAnnotation
		});

		// insert context menu item on 1 position
		items.splice(1, 0, {
			text: "Remove all annotations",
			action: removeAllAnnotation
		});

		// insert context menu separator
		items.splice(2, 0, undefined);

		return items;
	}

	function setToolbarButtonActive(type, markerType) {
		var $buttons = $('.btn[data-annotation-type]');
		$buttons.removeClass('active');
		$buttons.blur();

		if (type) {
			var selector = '.btn[data-annotation-type="' + type + '"]';
			if (markerType) selector += '[data-marker-type="' + markerType + '"]';
			$(selector).addClass('active');
		}
	}

	function updatePropertiesBySelectedAnnotation(strokeWidth, strokeType) {
		var strokeColor;
		var annotation = chart.annotations().getSelectedAnnotation();
		if (annotation == null) return;

		if (typeof annotation.stroke() === 'function') {
			strokeColor = annotation.color();
		} else {
			strokeColor = annotation.stroke().color;
		}

		switch (strokeType) {
			case '6' :
				strokeType = null;
				break;
			case '7' :
				strokeType = '1 1';
				break;
			case '8' :
				strokeType = '10 5';
				break;
		}

		var settings = {
			thickness: strokeWidth,
			color: strokeColor,
			dash: strokeType
		};

		annotation.stroke(settings);
		annotation.hoverStroke(settings);
		annotation.selectStroke(settings);
	}

	function hidePreloader() {
		$('#loader-wrapper').fadeOut('slow');
	}

	function initTooltip(position) {
		$(document).ready(function () {
			$('[data-toggle="tooltip"]').tooltip({
				'placement': position,
				'animation': false
			});
		});
	}

	$(document).ready(function () {

		$('select.choose-drawing-tools').on('change', changeAnnotations);
		$('select.choose-marker').on('change', changeAnnotations);
		$('[data-annotation-type]').on('click', changeAnnotations);

		function changeAnnotations() {
			var $that = $(this);

			setTimeout(function () {
				var $target = $that;
				var active = $target.hasClass('active');
				var $markerSize = $('#select-marker-size');
				var markerSize = $markerSize.val();

				if (active) {
					chart.annotations().cancelDrawing();
					setToolbarButtonActive(null);
				} else {
					var type = $target.data().annotationType || $target.find('option:selected').data().annotationType;

					if (!$target.data().annotationType) {
						var markerType = $target.find('option:selected').data().markerType;
					}

					setToolbarButtonActive(type, markerType);

					if (type) {

						if (!$target.data().annotationType) {
							var markerAnchor =  $target.find('option:selected').data().markerAnchor;
						}

						var drawingSettings = {
							type: type,
							size: markerSize,
							color: annotationsColor,
							markerType: markerType,
							anchor: markerAnchor
						};
						chart.annotations().startDrawing(drawingSettings);
					}
				}

				var annotation = chart.annotations().getSelectedAnnotation();
				if (annotation.fill === undefined) {
					$('.color-picker[data-color="fill"]').attr('disabled', 'disabled');
				} else {
					$('.color-picker[data-color="fill"]').removeAttr('disabled');
				}
			}, 1);
		}

		$('.btn[data-action-type]').click(function (evt) {
			var annotation = chart.annotations().getSelectedAnnotation();
			var $target = $(evt.currentTarget);
			$target.blur();
			var type = $target.attr('data-action-type');

			switch (type) {
				case 'removeAllAnnotations':
					removeAllAnnotation();
					break;
				case 'removeSelectedAnnotation' :
					removeSelectedAnnotation();
					break;
				case 'unSelectedAnnotation' :
					chart.annotations().unselect(annotation).cancelDrawing();
					setToolbarButtonActive(null);
					break;
			}

		});

		$('#select-stroke-settings').on('change', function () {
			var strokeWidth;
			var strokeType;
			var STROKE_WIDTH = 1;

			if ($(this).val()) {
				switch ($(this).val()[0]) {
					case '6' :
					case '7' :
					case '8' :
						strokeType = $(this).val()[0];
						strokeWidth = $(this).val()[1] || STROKE_WIDTH;
						break;
					default :
						strokeType = $(this).val()[1];
						strokeWidth = $(this).val()[0];
						break;
				}
				updatePropertiesBySelectedAnnotation(strokeWidth, strokeType);
			}
		});

		$('#select-marker-size').on('change', function () {
			var annotation = chart.annotations().getSelectedAnnotation();

			if (annotation == null) return;

			if (annotation.type === 'marker') {
				annotation.size($(this).val());
			}
		});


		$chartDiv.keyup(function (e) {
			if (e.keyCode == 8 || e.keyCode == 46) {
				removeSelectedAnnotation();
			}
		})
	});
	
});
