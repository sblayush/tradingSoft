import os

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
		print('Error in Write Data: ' + str(e))
	
def readData(dataPath):
	try:
		global stocks
		full_path = os.path.realpath(__file__)
		stockFile = os.path.dirname(full_path) + dataPath
		saveFile = open(stockFile,'r')
		stocks = saveFile.read()
		stocks = stocks.split('\n')
		stocks = stocks[:-1]
		saveFile.close()
		
		return stocks
		
	except Exception as e:
		print('Error in Read Data: ' + str(e))
		