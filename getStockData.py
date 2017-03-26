from updateFunctions import importRawDataFromCSV
import os
import pandas as pd
from pandas import DataFrame
import json

def getStockData(stockName):
	full_path = os.path.realpath(__file__)
	stockFile = os.path.dirname(full_path) + '\\Shares\\' + stockName + '.csv'
	df = pd.read_csv(stockFile, names = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], header = None)
	df.Date = pd.to_datetime(df.Date)
	df.Date = df.Date.dt.strftime('%Y-%m-%d')
	data = df.values.tolist()
	try:
		stockFile = os.path.dirname(full_path) + '\\annotations\\' + stockName + '.txt'
		with open(stockFile) as file:
			annotations = json.load(file)
	except Exception as e:
		annotations = {}
	returnObject = {
		'data' : data,
		'annotations' : annotations
	}
	return returnObject
	
if __name__ == "__main__":
	print(getStockData('AURIONPRO')['annotations'])
	