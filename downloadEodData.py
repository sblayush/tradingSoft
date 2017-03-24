import requests, zipfile, io
import pandas as pd
import datetime

def downloadEodData(Date):
	year = Date.strftime('%Y')
	month = Date.strftime('%b').upper()
	compdate = Date.strftime('%d%b%Y').upper()
	zip_file_url = 'http://nseindia.com/content/historical/EQUITIES/'+year+'/'+month+'/cm'+compdate+'bhav.csv.zip'
	r = requests.get(zip_file_url)
	if r.ok == True:
		z = zipfile.ZipFile(io.BytesIO(r.content))
		file = z.open('cm'+compdate+'bhav.csv')
		df = pd.read_csv(file, index_col = 'SYMBOL', usecols = ['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'TOTTRDQTY'])
		df.rename(columns={'TOTTRDQTY': 'Volume'}, inplace=True)
		df.rename(columns={'OPEN': 'Open'}, inplace=True)
		df.rename(columns={'HIGH': 'High'}, inplace=True)
		df.rename(columns={'LOW': 'Low'}, inplace=True)
		df.rename(columns={'CLOSE': 'Close'}, inplace=True)
		df = df.reset_index().drop_duplicates(subset='SYMBOL', keep = 'first').set_index('SYMBOL')
		return df
	else:
		return
		
if __name__ == "__main__":
	#Date = datetime.datetime.now()
	Date2 = datetime.date(2017,3,15)
	downloadEodData(Date2)

	#https://nseindia.com/content/historical/EQUITIES/2017/MAR/cm15MAR2017bhav.csv.zip