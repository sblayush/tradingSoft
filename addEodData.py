import pandas as pd
import os
import csv


#http://www.extendoffice.com/documents/excel/613-excel-export-to-csv-file.html#selection-to-csv
def addEodData(ticker):
	full_path = os.path.realpath(__file__)
	stockFile = os.path.dirname(full_path) + '\Indicators\\' + ticker + '.csv'
	df = pd.read_csv(stockFile, index_col = 'SYMBOL', usecols = ['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'TOTTRDQTY'])
	df.rename(columns={'TOTTRDQTY': 'Volume'}, inplace=True)
	df.rename(columns={'OPEN': 'Open'}, inplace=True)
	df.rename(columns={'HIGH': 'High'}, inplace=True)
	df.rename(columns={'LOW': 'Low'}, inplace=True)
	df.rename(columns={'CLOSE': 'Close'}, inplace=True)
	
	return df
	
#addEodData('cm22JAN2016bhav')