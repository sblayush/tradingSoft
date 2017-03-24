from readWriteData import readData
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
		
def getSharesList(fileName):
	stocks = readData('\\stocks\\' + fileName)
	shares = []
	for ticker in stocks:
		shares.append(ticker)
	return shares
	
def getAllSharesList():
	fileList = os.listdir(dir_path+"\\Shares")
	with open(dir_path + '\\stocks\\allStocks.txt', 'w') as the_file:
		for file in fileList:
			the_file.write(file[:-4] + '\n')
			
	allSharesList = getSharesList('allStocks.txt')
	return allSharesList
	

def getMyPortfolioSharesList():
	myPortfolioSharesList = getSharesList('myPortfolioStocks.txt')
	return myPortfolioSharesList
