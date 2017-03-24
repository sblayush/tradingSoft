from readWriteData import readData
from update import update

def findPoints():
	try:
		stocks = readData('\\stocks\\myPortfolioStocks.txt')
		indicatorsObject = {
			'SMAPoints' : [],
			'ADLPoints' : [],
			'ADXPoints' : [],
			'trendPoints' : [],
			'closePoints' : [],
			'highPoints' : [],
			'lowPoints' : []
		}
		
		for ticker in stocks:
			f = update(ticker)
			#print(f)
			
			"""
			stoploss = 1#((f['ADL_SMA_14'][-1]-f['ADL'][-2])*(f['High'][-1]-f['Low'][-1])+(f['High'][-1]+f['Low'][-1])*f['Volume'][-1])/(2*f['Volume'][-1])
			avgADX = float(f['PLUS_DI'][-1])+float(f['MINUS_DI'][-1]+f['ADX'][-1])
			diff1 = (f['PLUS_DI'][-1]-f['MINUS_DI'][-1])/avgADX
			diff2 = (f['PLUS_DI'][-1]-f['ADX'][-1])/avgADX
			diff3 = (f['ADX'][-1]-f['MINUS_DI'][-1])/avgADX
			
			if (f['EMA_14'][-2] > f['SMA_20'][-2] and f['EMA_14'][-1] < f['SMA_20'][-1]):
				indicatorsObject['SMAPoints'].append({'ticker':ticker, 'direction':'down', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			elif (f['EMA_14'][-1] > f['SMA_20'][-1] and f['EMA_14'][-2] < f['SMA_20'][-2]):
				indicatorsObject['SMAPoints'].append({'ticker':ticker, 'direction':'up', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			if (f['ADL'][-2] > f['ADL_SMA_14'][-2] and f['ADL'][-1] < f['ADL_SMA_14'][-1]):
				indicatorsObject['ADLPoints'].append({'ticker':ticker, 'direction':'down', 'close':float(f['Close'][-1]), 'stoploss':stoploss})
			elif (f['ADL'][-1] > f['ADL_SMA_14'][-1] and f['ADL'][-2] < f['ADL_SMA_14'][-2]):
				indicatorsObject['ADLPoints'].append({'ticker':ticker, 'direction':'up', 'close':float(f['Close'][-1]), 'stoploss':stoploss})
			if (f['PLUS_DI'][-2] > f['MINUS_DI'][-2] and f['PLUS_DI'][-1] < f['MINUS_DI'][-1]):
				indicatorsObject['ADXPoints'].append({'ticker':ticker, 'direction':'down', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			elif (f['PLUS_DI'][-1] > f['MINUS_DI'][-1] and f['PLUS_DI'][-2] < f['MINUS_DI'][-2]):
				indicatorsObject['ADXPoints'].append({'ticker':ticker, 'direction':'up', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			if (f['MINUS_DI'][-2] < f['ADX'][-2] and f['MINUS_DI'][-1] > f['ADX'][-1]):
				indicatorsObject['trendPoints'].append({'ticker':ticker, 'direction':'down', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			elif (f['PLUS_DI'][-1] > f['ADX'][-1] and f['PLUS_DI'][-2] < f['ADX'][-2]):
				indicatorsObject['trendPoints'].append({'ticker':ticker, 'direction':'up', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			if ((diff1 < 0.05 and diff1 > -0.05) and (diff2 < 0.05 and diff2 > -0.05) and (diff3 < 0.05 and diff3 > -0.05)):
				indicatorsObject['closePoints'].append({'ticker':ticker, 'direction':'up', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			"""
			if (f['High'][-4] <= f['High'][-3] and f['High'][-3] > f['High'][-2] and f['High'][-2] > f['High'][-1]):
				indicatorsObject['highPoints'].append({'ticker':ticker, 'direction':'down', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			if (f['Low'][-4] >= f['Low'][-3] and f['Low'][-3] < f['Low'][-2] and f['Low'][-2] < f['Low'][-1]):
				indicatorsObject['lowPoints'].append({'ticker':ticker, 'direction':'down', 'close':float(f['Close'][-1]), 'stoploss':'-'})
			
		return indicatorsObject
		
	except Exception as e:
		print('Error in Finding Points: ' + str(e))

#findPoints()	