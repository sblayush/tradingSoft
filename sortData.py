from updateFunctions import importRawDataFromCSV
import datetime, os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def sortData():
	try:
		successFiles = []
		full_path = os.path.realpath(__file__)
		direc = os.path.dirname(full_path) + '\Shares'
		l = os.listdir(direc)
		for file in l:
			df = importRawDataFromCSV(file)
			df = df.reset_index()
			df['Date'] = pd.to_datetime(df.Date)
			df = df.sort(columns = 'Date').set_index('Date')
			stockFile = os.path.dirname(full_path) + '\Shares\\' + file
			df.to_csv(stockFile, header = False)
			successFiles.append(file)
		logger.info(successFiles)
		successString = 'Sorting data Successful!'
		logger.info(successString)
		return successString
		
	except Exception as e:
		errorString = 'Error in sortData: ' + str(e)
		logger.error(errorString)
		return errorString

if __name__ == "__main__":
	print(sortData())