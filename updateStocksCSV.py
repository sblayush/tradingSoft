from downloadEodData import downloadEodData
from readWriteData import writeData
import os

def updateStocksCSV(Date):
	try:
		df = downloadEodData(Date)
		for symbol in df.index:
			full_path = os.path.realpath(__file__)
			stockFile = os.path.dirname(full_path) + '\Shares\\' + symbol + '.csv'
			file = open(stockFile, 'a+')
			file.write(Date.strftime('%d-%b-%y')+','+str(df['Open'][symbol])+','+str(df['High'][symbol])+','+str(df['Low'][symbol])+','+str(df['Close'][symbol])+','+str(df['Volume'][symbol])+'\n')
			file.close()
			
		writeData('\\Stocks\\DatesUpadted.txt', Date.strftime('%d-%b-%y')+'\n')
		print('Successful: '+ Date.strftime('%d-%b-%y'))
		
	except Exception as e:
		print('Data for ' + Date.strftime('%d-%b-%y') + ' does not exists!')
		