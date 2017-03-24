import os
import json

def saveAnnotations(shareName, annotationsString):
	full_path = os.path.realpath(__file__)
	filePath = os.path.dirname(full_path) + '\\annotations\\' + shareName + '.txt'
	with open(filePath, "w") as f:
		json.dump(json.loads(annotationsString), f, indent = 4, ensure_ascii=False)
	return('Save annotations successful')
	
if __name__ == "__main__":
	saveAnnotations('hg')