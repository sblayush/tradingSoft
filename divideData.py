import datetime, os
from updateFunctions import importRawDataFromCSV
import pandas as pd
from pandas import DataFrame
import logging

logger = logging.getLogger(__name__)

def divideData():
	try:
		i = str(raw_input('Input the date in the format dd/mm/yy: '))
		try:
			divideDate = datetime.datetime.strptime(i, '%d/%m/%y').strftime('%d-%b-%y')
		except ValueError:
			logger.error("Incorrect date format in divideData")
		
		file = str(raw_input('Input the share name: '))
		full_path = os.path.realpath(__file__)
		df = importRawDataFromCSV(file + '.csv')
		try:
			symbol = str(raw_input('Input the symbol:\n1.Add (+)\n2.Substract (-)\n3.Divide (/)\n4.Multiply (*)\nInput: '))
			cf = {}
			
			logger.info(divideDate)
			logger.info(df.index[0])
			if symbol == '+':
				factor = float(str(raw_input('Input the factor to be added: ')))
				cf['Open'] = df.loc[df.index[0]:divideDate]['Open']+factor
				cf['High'] = df.loc[df.index[0]:divideDate]['High']+factor
				cf['Low'] = df.loc[df.index[0]:divideDate]['Low']+factor
				cf['Close'] = df.loc[df.index[0]:divideDate]['Close']+factor
				cf['Volume'] = df.loc[df.index[0]:divideDate]['Volume']
				
			elif symbol == '-':
				factor = float(str(raw_input('Input the factor to be substracted: ')))
				cf['Open'] = df.loc[df.index[0]:divideDate]['Open']-factor
				cf['High'] = df.loc[df.index[0]:divideDate]['High']-factor
				cf['Low'] = df.loc[df.index[0]:divideDate]['Low']-factor
				cf['Close'] = df.loc[df.index[0]:divideDate]['Close']-factor
				cf['Volume'] = df.loc[df.index[0]:divideDate]['Volume']
				
			elif symbol == '/':
				factor = float(str(raw_input('Input the factor to be divided: ')))
				cf['Open'] = df.loc[df.index[0]:divideDate]['Open']/factor
				cf['High'] = df.loc[df.index[0]:divideDate]['High']/factor
				cf['Low'] = df.loc[df.index[0]:divideDate]['Low']/factor
				cf['Close'] = df.loc[df.index[0]:divideDate]['Close']/factor
				cf['Volume'] = df.loc[df.index[0]:divideDate]['Volume']*factor
				
			elif symbol == '*':
				factor = float(str(raw_input('Input the factor to be multiplied: ')))
				cf['Open'] = df.loc[df.index[0]:divideDate]['Open']*factor
				cf['High'] = df.loc[df.index[0]:divideDate]['High']*factor
				cf['Low'] = df.loc[df.index[0]:divideDate]['Low']*factor
				cf['Close'] = df.loc[df.index[0]:divideDate]['Close']*factor
				cf['Volume'] = df.loc[df.index[0]:divideDate]['Volume']/factor
			
			df.update(cf, join = 'left', overwrite = True)
			
		except Exception as e:
			logger.error('Invalid input!!' + str(e))
			
		
		stockFile = os.path.dirname(full_path) + '\Shares\\' + file + '.csv'
		df.to_csv(stockFile, header = False)
		
		logger.info('Divide data Successful!')
		return 'Divide data Successful!'
		
	except Exception as e:
		logger.error('Error in divideData: ' + str(e))

#divideData()