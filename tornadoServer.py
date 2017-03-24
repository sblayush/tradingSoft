from tornado.web import RequestHandler, Application, StaticFileHandler
from runCommand import runCommand
import tornado.ioloop
import json
import os

dirPath = os.path.dirname(os.path.realpath(__file__))

class MainHandler(RequestHandler):
	def get(self, inputText):
		self.render(inputText)

class TestHandler(RequestHandler):
	def post(self):
		try:
			command = ""
			argumentsList = []
			responseMap = {}
			print("Got a request")
			receiveDataMap = json.loads(self.request.body.decode('utf-8'))
			if 'command' in receiveDataMap and 'argumentsList' in receiveDataMap:
				command = receiveDataMap['command']
				argumentsList = receiveDataMap['argumentsList']
				print('Got command : ' + command + ' and arguments : ' + str(argumentsList))
				try:
					returnValue = runCommand(command, argumentsList)
					responseMap = {
						'success' : returnValue
					}
				except Exception as e:
					print("Exception in running command " + command + " : " + str(e))
					responseMap = {
						'error' : str(e)
					}
			
			#print("Sending Back " + str(responseMap))
			self.set_header("Content-Type", "application/json")
			self.set_header("Access-Control-Allow-Origin","*")
			self.set_header("Access-Control-Expose-Headers: Access-Control-Allow-Origin","*")
			self.set_header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept","*")
			self.write(responseMap)
		except Exception as e:
			print("Exception in tornadoServer is:" + str(e))
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
	print("Server started at port: " + str(port) + "........")
	tornado.ioloop.IOLoop.current().start()
