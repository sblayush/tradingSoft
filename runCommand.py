from updateFunctions import getMyPortfolioSharesList, getAllSharesList
from saveMyPortfolioChanges import saveMyPortfolioChanges
from getLastUpdatedDate import getLastUpdatedDate
from removeDuplicates import removeDuplicates
from saveAnnotations import saveAnnotations
from saveProperties import saveProperties
from getStockData import getStockData
from dailyUpdate import dailyUpdate
from divideData import divideData
from findPoints import findPoints
from sortData import sortData
import logging

logger = logging.getLogger(__name__)

def runCommand(command, argumentsList):
	try:
		commandMap = {
			'dailyUpdate' : dailyUpdate,
			'findPoints' : findPoints,
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
		logger.info("Command " + command + "run successfully")
		return returnValue
	except Exception as e:
		logger.error('Exception in runCommand:' + str(e))
