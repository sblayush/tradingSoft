from tornado.web import RequestHandler, Application, StaticFileHandler
from runCommand import runCommand
from datetime import date
import logging.config
import tornado.ioloop
import json
import os

today = date.today()
today = today.strftime("%d_%m_%y")
dirPath = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename = dirPath + "/Logs/" + today + ".log",
					filemode = 'w',
					format = '%(asctime)s, %(name)s, %(levelname)s %(lineno)d : %(message)s',
					datefmt = '%H:%M:%S',
					level = logging.DEBUG)
logger = logging.getLogger(__name__)
logging.getLogger().addHandler(logging.StreamHandler())

class MainHandler(RequestHandler):
	def get(self, inputText):
		self.render(inputText)

class TestHandler(RequestHandler):
	def post(self):
		try:
			command = ""
			argumentsList = []
			responseMap = {}
			logger.info("Got a request")
			receiveDataMap = json.loads(self.request.body.decode('utf-8'))
			if 'command' in receiveDataMap and 'argumentsList' in receiveDataMap:
				command = receiveDataMap['command']
				argumentsList = receiveDataMap['argumentsList']
				logger.info('Got command : ' + command + ' and arguments : ' + str(argumentsList))
				try:
					returnValue = runCommand(command, argumentsList)
					responseMap = {
						'success' : returnValue
					}
				except Exception as e:
					logger.error("Exception in running command " + command + " : " + str(e))
					responseMap = {
						'error' : str(e)
					}
			
			self.set_header("Content-Type", "application/json")
			self.set_header("Access-Control-Allow-Origin","*")
			self.set_header("Access-Control-Expose-Headers: Access-Control-Allow-Origin","*")
			self.set_header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept","*")
			self.write(responseMap)
		except Exception as e:
			logger.error("Exception in tornadoServer is:" + str(e))
			raise
	
def make_app():
    return Application([
        (r"/runCommand", TestHandler),
		(r"/(.*)", StaticFileHandler, {"path": dirPath})
    ])

if __name__ == "__main__":
	app = make_app()
	port = 8888
	app.listen(port)
	logger.info("Server started at port: " + str(port) + "........")
	tornado.ioloop.IOLoop.current().start()
