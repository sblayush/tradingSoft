import datetime, os
from updateFunctions import importRawDataFromCSV
import pandas as pd

def sortData():
	try:
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
			print('Done ' + file)
		print('Operation Successful!')
		
	except Exception as e:
		print('Error in sortData: ' + str(e))

#sortData()