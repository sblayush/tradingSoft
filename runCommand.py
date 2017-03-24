from dateIteration import dateIteration
from sortData import sortData
from removeDuplicates import removeDuplicates
from divideData import divideData
from getStockData import getStockData
from getSharesList import getMyPortfolioSharesList, getAllSharesList
from saveMyPortfolioChanges import saveMyPortfolioChanges
from findPoints import findPoints
from getLastUpdatedDate import getLastUpdatedDate
from saveProperties import saveProperties
from saveAnnotations import saveAnnotations

def runCommand(command, argumentsList):
	try:
		commandMap = {
			'dateIteration' : dateIteration,
			'getPoints' : findPoints,
			'sortData' : sortData,
			'removeDuplicates' : removeDuplicates,
			'divideData' : divideData,
			'getStockData' : getStockData,
			'getMyPortfolioSharesList' : getMyPortfolioSharesList,
			'getAllSharesList' : getAllSharesList,
			'saveMyPortfolioChanges' : saveMyPortfolioChanges,
			'getLastUpdatedDate' : getLastUpdatedDate,
			'saveProperties' : saveProperties,
			'saveAnnotations' : saveAnnotations
			}
			
		returnValue = commandMap[command](*argumentsList)
		return returnValue
	except Exception as e:
		print ('Exception in runCommand:' +	str(e))
