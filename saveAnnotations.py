import os
import json
import logging

logger = logging.getLogger(__name__)

def saveAnnotations(shareName, annotationsString):
	full_path = os.path.realpath(__file__)
	filePath = os.path.dirname(full_path) + '\\annotations\\' + shareName + '.txt'
	try:
		with open(filePath, "w") as f:
			json.dump(json.loads(annotationsString), f, indent = 4, ensure_ascii=False)
		successMsg =  'Save annotations successful'
		logger.info(successMsg)
		return successMsg
	except Exception as e:
		logger.error('Exception in saveAnnotations:' + str(e))
		return 'Exception in saveAnnotations'
	
if __name__ == "__main__":
	print(saveAnnotations('hg'))