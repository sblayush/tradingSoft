import datetime, os
from updateFunctions import importRawDataFromCSV

def removeDuplicates():
	try:
		full_path = os.path.realpath(__file__)
		direc = os.path.dirname(full_path) + '\Shares'
		l = os.listdir(direc)
		for file in l:
			df = importRawDataFromCSV(file)
			df = df.reset_index().drop_duplicates(subset='Date', keep = 'first').set_index('Date')
			stockFile = os.path.dirname(full_path) + '\Shares\\' + file
			df.to_csv(stockFile, header = False)
			print('Done ' + file)
		print('Operation Successful!')
		
	except Exception as e:
		print('Error in removeDuplicates: ' + str(e))
	
#removeDuplicates()