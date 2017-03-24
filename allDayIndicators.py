from findPoints import findPoints
#from tabulate import tabulate
from datetime import datetime
from time import sleep
from readWriteData import writeData
from writeDataToHTML import writeDataToHTML

def allDayIndicators():
	try:
		oldSMAtable = []
		oldADLtable = []
		oldADXtable = []
		oldTrendTable = []
		oldCloseTable = []
		
		endOfTradingTimeString = '16:01:00'
		endOfTradingTime = datetime.strptime(endOfTradingTimeString, '%H:%M:%S').strftime('%H:%M:%S')
		startOfTradingTimeString = '09:15:00'
		startOfTradingTime = datetime.strptime(startOfTradingTimeString, '%H:%M:%S').strftime('%H:%M:%S')
		presentTime = datetime.now().strftime('%H:%M:%S')
		
		headers = ["      ", "Share", "Direction", "Close", "StopLoss", "Trend"]
		
		#while presentTime < endOfTradingTime:
		while (True):
			SMAPoints, ADLPoints, ADXPoints, trendPoints, closePoints, highPoints, lowPoints = findPoints()

			presentTime = datetime.now().strftime('%H:%M:%S')
			presentDate = datetime.now().strftime('%d-%m-%Y')
			
			SMAtable = []
			ADLtable = []
			ADXtable = []
			trendTable = []
			closeTable = []
			
			for point in SMAPoints:
				SMAtable.append(['SMA', point['ticker'], point['direction'], point['close'], point['stoploss'], 'no'])
			for point in ADLPoints:
				ADLtable.append(['ADL', point['ticker'], point['direction'], point['close'], point['stoploss'], 'no'])
			for point in ADXPoints:
				ADXtable.append(['ADX', point['ticker'], point['direction'], point['close'], point['stoploss'], 'no'])
			for point in trendPoints:
				trendTable.append(['Trend', point['ticker'], point['direction'], point['close'], point['stoploss'], 'no'])
			for point in closePoints:
				closeTable.append(['StopLoss', point['ticker'], point['direction'], point['close'], point['stoploss'], 'no'])
			
			for row in oldSMAtable:
				if row in SMAtable:
					continue
				elif row[5] == 'change':
					if len([row2 for row2 in SMAtable if row[1] == row2[1]]) > 0:
						continue
					else:
						SMAtable.append(['ADL', row[1], row[2], row[3], row[4], 'change'])
				else:
					SMAtable.append(['SMA', row[1], row[2], row[3], row[4], 'change'])
			
			for row in oldADLtable:
				if row in ADLtable:
					continue
				elif row[5] == 'change':
					if len([row2 for row2 in ADLtable if row[1] == row2[1]]) > 0:
						continue
					else:
						ADLtable.append(['ADL', row[1], row[2], row[3], row[4], 'change'])
				else:
					ADLtable.append(['ADL', row[1], row[2], row[3], row[4], 'change'])
				
			for row in oldADXtable:
				if row in ADXtable:
					continue
				elif row[5] == 'change':
					if len([row2 for row2 in ADXtable if row[1] == row2[1]]) > 0:
						continue
					else:
						ADXtable.append(['ADL', row[1], row[2], row[3], row[4], 'change'])
				else:
					ADXtable.append(['ADX', row[1], row[2], row[3], row[4], 'change'])
					
			for row in oldTrendTable:
				if row in trendTable:
					continue
				elif row[5] == 'change':
					if len([row2 for row2 in trendTable if row[1] == row2[1]]) > 0:
						continue
					else:
						trendTable.append(['ADL', row[1], row[2], row[3], row[4], 'change'])
				else:
					trendTable.append(['Trend', row[1], row[2], row[3], row[4], 'change'])
			
			for row in oldCloseTable:
				if row in closeTable:
					continue
				elif row[5] == 'change':
					if len([row2 for row2 in closeTable if row[1] == row2[1]]) > 0:
						continue
					else:
						closeTable.append(['ADL', row[1], row[2], row[3], row[4], 'change'])
				else:
					closeTable.append(['StopLoss', row[1], row[2], row[3], row[4], 'change'])
				
			
			oldSMAtable = SMAtable
			oldADLtable = ADLtable
			oldADXtable = ADXtable
			oldTrendTable = trendTable
			oldCloseTable = closeTable
			
			table = SMAtable + ADLtable + ADXtable + trendTable + closeTable
			
			writeData('\\Stocks\\DailyLog\\' + presentDate + '.txt', presentTime+'\n')
			#writeData('\\Stocks\\DailyLog\\' + presentDate + '.txt', tabulate(table, headers)+'\n\n')
			#writeData(presentDate, presentTime+'\n')
			#writeData(presentDate, tabulate(table, headers)+'\n\n')
			print(presentTime)
			#print endOfTradingTime
			#print(tabulate(table, headers, tablefmt="fancy_grid"))
			
			writeDataToHTML('\\html\\indicators.html', table);
			
			#if presentTime > endOfTradingTime:
			#	break
			#sleep(150)
			
		print('Day Ended!!')
	except Exception as e:
		print('Error in allDayIndicators:' + str(e))

#allDayIndicators()