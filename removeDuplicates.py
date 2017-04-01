import datetime, os
from updateFunctions import importRawDataFromCSV
import logging

logger = logging.getLogger(__name__)

def removeDuplicates():
	try:
		full_path = os.path.realpath(__file__)
		direc = os.path.dirname(full_path) + '\Shares'
		l = os.listdir(direc)
		successFiles = []
		for file in l:
			df = importRawDataFromCSV(file)
			df = df.reset_index().drop_duplicates(subset='Date', keep = 'first').set_index('Date')
			stockFile = os.path.dirname(full_path) + '/Shares/' + file
			df.to_csv(stockFile, header = False)
			successFiles.append(file)
		logger.info("Removed duplicates for files: " + str(successFiles))
		return "Remove duplicates successful"
		
	except Exception as e:
		errorString = 'Error in removeDuplicates: ' + str(e)
		logger.error(errorString)
		return errorString
	
if __name__ == "__main__":
	removeDuplicates()