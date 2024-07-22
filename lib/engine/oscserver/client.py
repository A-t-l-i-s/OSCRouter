from engine.require import *





__all__ = ("OSCServer_Client",)





class OSCServer_Client(RFT_Object):
	def __init__(self, ip:str, port:int):
		# ~~~~~~~ Variables ~~~~~~
		self.ip = ip
		self.port = port
		# ~~~~~~~~~~~~~~~~~~~~~~~~

		# Create client
		self.client = OSC_Client(
			self.ip,
			self.port
		)


	def trigger(self, address:str, values:tuple):
		try:
			# Send data to client
			self.client.send_message(
				address,
				values
			)

		except:
			# Print exception
			RFT_Exception.Traceback().print()


