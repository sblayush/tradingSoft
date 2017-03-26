import json, os

def saveProperties(propertiesJSON):
	try:
		full_path = os.path.realpath(__file__)
		filePath = os.path.dirname(full_path) + '\\UI\\propertiesFile.properties'
		with open(filePath, "w") as f:
			json.dump(json.loads(propertiesJSON), f, indent = 4, ensure_ascii=False)
		return "Properties saved successfully"
	except Exception as e:
		errorString = "Error in saving properties:" + str(e)
		logger.error(errorString)
		return errorString

if __name__ == "__main__":
	propertiesJSON = """{
		"EMArange" : 14,
		"SMArange" : 21,
		"datesRange": 150
	}
	"""
	saveProperties(propertiesJSON)