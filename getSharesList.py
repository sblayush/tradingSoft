import os

dir_path = os.path.dirname(os.path.realpath(__file__))
		
def getSharesList(fileName):
	stockFile = dir_path + "\\stocks\\" +fileName
	with open(stockFile,'r') as shareFile:
		stocks = shareFile.read()
		stocks = stocks.split('\n')
		stocks = stocks[:-1]
	return stocks
	
def getAllSharesList():
	allSharesList = getSharesList('allStocks.txt')
	return allSharesList
	
def getMyPortfolioSharesList():
	myPortfolioSharesList = getSharesList('myPortfolioStocks.txt')
	return myPortfolioSharesList

if __name__ == "__main__":
	print(getSharesList('myPortfolioStocks.txt'))