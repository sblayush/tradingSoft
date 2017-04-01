from readWriteData import writeData
import logging

logger = logging.getLogger(__name__)

def saveMyPortfolioChanges(mySharesList):
	try:
		filePath = '/stocks/myPortfolioStocks.txt'
		writeData(filePath, mySharesList[0]+'\n', shouldAppend=False)
		for share in mySharesList[1:]:
			writeData(filePath, share+'\n')
		successMsg = 'success in saveMyPortfolioChanges'
		logger.info(successMsg)
		return successMsg

	except Exception as e:
		logger.error('Exception in saveMyPortfolioChanges:' + str(e))
		return 'Exception in saveMyPortfolioChanges'