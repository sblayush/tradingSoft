from readWriteData import writeData

def saveMyPortfolioChanges(mySharesList):
	filePath = '\\stocks\\myPortfolioStocks.txt'
	writeData(filePath, mySharesList[0]+'\n', shouldAppend=False)
	for share in mySharesList[1:]:
		writeData(filePath, share+'\n')
	return 'success in saveMyPortfolioChanges'