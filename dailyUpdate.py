from datetime import timedelta, datetime
from updateStocksCSV import updateStocksCSV
import logging

logger = logging.getLogger(__name__)

def dateRange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)+1):
        yield start_date + timedelta(n)

def dailyUpdate(inputDate):
	try:
		start_date = datetime.strptime(inputDate, '%d/%m/%Y')
		start_date += timedelta(days=1)
	except ValueError:
		logger.error("Incorrect date format")
	logger.info("Got date: " + inputDate)
	end_date = datetime.now()
	
	try:
		for single_date in dateRange(start_date, end_date):
			updateStocksCSV(single_date)
		successString = "Successful dailyUpdate"
		logger.info(successString)
		return successString
	except Exception as e:
		logger.error('Exception in dailyUpdate:' + str(e))
		
if __name__ == "__main__":
	dailyUpdate('25/03/2017')