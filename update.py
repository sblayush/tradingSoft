from updateFunctions import *

error_stocks = []
def update(ticker):
	try:
		#df = importRawDataFromWeb(ticker)
		#df = makeStandardDataFrameFromWeb(df)
		df = importRawDataFromCSV(ticker+'.csv')
		#df = addUpdatedData(ticker+'.ns', df)
		#df = addIndicators(df)		
		#print 'Updating ', ticker, '...'
		#print df
		return df

	except Exception as e:
		print('Error in Update: ' + str(e))
		error_stocks.append(ticker)

#update('reliance')	
#update(sys.argv[1])
#stocksToPull = readData('\\stocks\\yahooStocks.txt')
#for stock in stocksToPull:
#	update(stock)
	
#print 'Error in updating:', error_stocks