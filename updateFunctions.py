import pandas_datareader.data as web
import datetime
#import talib
import numpy as np
import pandas as pd
from pandas import DataFrame
from readWriteData import readData
import os	
import xlrd
import csv
from urllib.request import urlopen

def importRawDataFromExcel():
	stocksToPull = readData('\\stocks\\excelStocks.txt')
	full_path = os.path.realpath(__file__)
	stockFile = os.path.dirname(full_path) + '\Indicators\\' + 'AllIndicators.xlsm'
	book = xlrd.open_workbook(stockFile)

	for ticker in stocksToPull:
		try:
			csvFile = os.path.dirname(full_path) + '\Indicators\\' + ticker +'.csv'
			sheet = book.sheet_by_name(ticker)
			your_csv_file = open(csvFile, 'wb')
			wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
			titleRow = ["Date","Open","High","Low","Close","Volume"]
			wr.writerow(titleRow)
			count = 0
			for row in sheet.col(0):
				oneRow = []
				if count < 2:
					count += 1
					continue
				if row.value != '':
					date = xlrd.xldate.xldate_as_datetime(row.value, book.datemode).strftime('%d-%b-%y')
					oneRow.append(date)
					oneRow.extend(sheet.row_values(count,start_colx=1, end_colx=6))
					wr.writerow(oneRow)
					count += 1
		except Exception as e:
			print('Cannot import data for:' + ticker)
			
def importRawDataFromCSV(ticker):
	full_path = os.path.realpath(__file__)
	stockFile = os.path.dirname(full_path) + '\Shares\\' + ticker
	df = pd.read_csv(stockFile, names = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], header = None, index_col = 'Date')
	return df
	
	
def makeStandardDataFrameFromCSV(df):
	try:
		df.drop('Turnover (Rs. Cr)', axis=1, inplace=True)
		df.rename(columns={'Shares Traded': 'Volume'}, inplace=True)
	except:
		print('Already Updated...')
	df.index = pd.to_datetime(df.index, format='%d-%b-%y')
	df.index.name = 'Date'
	return df
	
	
def importRawDataFromWeb(ticker):
	start = datetime.datetime(2014,1,1)
	df = web.DataReader(ticker,'yahoo',start)
	return df
	
	
def makeStandardDataFrameFromWeb(df):
	df.drop('Adj Close', axis=1, inplace=True)
	return df
	
	
def addIndicators(df):	
	volume = []
	"""
	for vol in df['Volume']:
		volume.append(float(vol))
	df['SMA_20'] = talib.SMA(np.asarray(df['Close']), 20)
	df['EMA_14'] = talib.EMA(np.asarray(df['Close']), 14)
	df['SMA_50'] = talib.SMA(np.asarray(df['Close']), 50)
	df['ADL'] = talib.AD(np.asarray(df['High']),np.asarray(df['Low']),np.asarray(df['Close']),np.asarray(volume))
	df['ADL_SMA_14'] = talib.SMA(np.asarray(df['ADL']), 14)
	df['ADX'] = talib.ADX(np.asarray(df['High']),np.asarray(df['Low']),np.asarray(df['Close']), 14) 
	df['PLUS_DI'] = talib.PLUS_DI(np.asarray(df['High']),np.asarray(df['Low']),np.asarray(df['Close']), 14) 
	df['MINUS_DI'] = talib.MINUS_DI(np.asarray(df['High']),np.asarray(df['Low']),np.asarray(df['Close']), 14) 
	df['UBAND'], df['MBAND'], df['LBAND'] = talib.BBANDS(np.asarray(df['Close']), 20)
	"""
	return df	

	
def storeDataFrameToCSV(df, ticker):
	full_path = os.path.realpath(__file__)
	stockFile = os.path.dirname(full_path) + '\Indicators\\' + ticker + '.csv'
	df.to_csv(stockFile)
	
def addUpdatedData(stock, df):
	try:
		urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1d/csv'
		sourceCode = urlopen(urlToVisit).read()
		splitSource = sourceCode.split('\n')
		
		data = {}
		vol = 0
		for eachLine in splitSource:
			splitLine = eachLine.split(',')
			if len(splitLine) == 6:
				if 'values' not in eachLine:
					if 'labels' not in eachLine:
						vol = vol + float(splitLine[5])
		
		data['Open'] = float(splitSource[17].split(',')[1])
		data['High'] = float(splitSource[13].split(',')[1])
		data['Low'] = float(splitSource[14].split(',')[0].split(':')[1])
		data['Close'] = float(splitSource[-2].split(',')[4])
		data['Date'] = datetime.datetime.fromtimestamp(int(splitSource[-2].split(',')[0])).strftime('%d-%m-%Y')
		data['Volume'] = vol
		Date = datetime.datetime.strptime(data['Date'],'%d-%m-%Y').strftime("%d-%b-%y")
		del data['Date']
		d = DataFrame(data, index = [Date])
		df.loc[Date] = d.loc[Date]
		return df
		
	except Exception as e:
		print('Error in addUpdatedData: ',str(e))
		
		