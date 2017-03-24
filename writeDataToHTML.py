import os
def writeDataToHTML(dataPath, data):
	try:
		full_path = os.path.realpath(__file__)
		stockFile = os.path.dirname(full_path) + dataPath
		saveFile = open(stockFile,'w')
		
		htmlContent = '<head><link rel="stylesheet" type="text/css" href="mystyle.css"><meta http-equiv="refresh" content="20" ></head><body>'
		htmlContent += '<table><thead><tr><th>SHARE</th><th>INDICATOR</th><th>DIRECTION</th><th>CLOSING PRICE</th><th>STOPLOSS</th><th>CHANGE</th></tr></thead><tbody>'
		for row in data:
			htmlContent += '<tr><td>' + row[1] + '</td><td>' + row[0] + '</td><td class = "' + row[2] + '-direction">' + row[2] + '</td><td>' + str(row[3]) +  '</td><td>' + str(row[4]) +  '</td><td class = "' + row[5] + '-direction">' + row[5] + '</td></tr>'
		htmlContent += '</tbody></table>'
		htmlContent += '</body></html>'
		
		saveFile.write(htmlContent)
		saveFile.close()
		
	except Exception as e:
		print('Error in writeDataToHTML: ' + str(e))
		
		