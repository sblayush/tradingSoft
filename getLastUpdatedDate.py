import os

def getLastUpdatedDate():
	full_path = os.path.realpath(__file__)
	stockFile = os.path.dirname(full_path) + '\\stocks\\DatesUpadted.txt'
	with open(stockFile, 'rb') as fh:
		for line in fh:
			pass
		lastUpdatedDate = line.decode("utf-8")
	lastUpdatedDate = str(lastUpdatedDate).strip('\n')
	return lastUpdatedDate
	
if __name__ == "__main__":
	getLastUpdatedDate()
	