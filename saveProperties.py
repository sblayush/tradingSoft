import json, os

def saveProperties(propertiesJSON):
	full_path = os.path.realpath(__file__)
	filePath = os.path.dirname(full_path) + '\\UI\\propertiesFile.properties'
	with open(filePath, "w") as f:
		json.dump(json.loads(propertiesJSON), f, indent = 4, ensure_ascii=False)

if __name__ == "__main__":
	propertiesJSON = """{
		"EMArange" : 14,
		"SMArange" : 21
	}
	"""
	saveProperties(propertiesJSON)