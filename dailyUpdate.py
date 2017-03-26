from datetime import timedelta, date, datetime
from updateStocksCSV import updateStocksCSV

def dateRange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)+1):
        yield start_date + timedelta(n)

def dailyUpdate(inputDate):
	#inputDate = str(raw_input('Input the start date in the format dd/mm/yy: '))
	try:
		start_date = datetime.strptime(inputDate, '%d/%m/%Y')
	except ValueError:
		print( "Incorrect format")
	print("Got date: " + inputDate)
	end_date = datetime.now()
	
	for single_date in dateRange(start_date, end_date):
		updateStocksCSV(single_date)
	