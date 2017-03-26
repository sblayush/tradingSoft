import os
import logging

logger = logging.getLogger(__name__)

def writeData(dataPath, data, shouldAppend=True):
	try:
		full_path = os.path.realpath(__file__)
		stockFile = os.path.dirname(full_path) + dataPath
		if(shouldAppend):
			saveFile = open(stockFile,'a')
		else:
			saveFile = open(stockFile,'w')
		saveFile.write(data)
		saveFile.close()
		
	except Exception as e:
		logger.error('Error in Write Data: ' + str(e))
	
	
def readData(dataPath):
	try:
		full_path = os.path.realpath(__file__)
		stockFile = os.path.dirname(full_path) + dataPath
		saveFile = open(stockFile,'r')
		data = saveFile.read()
		saveFile.close()
		return data
		
	except Exception as e:
		logger.info('Error in Read Data: ' + str(e))
		
		
if __name__ == "__main__":
	print(readData('\\stocks\\myPortfolioStocks.txt'))