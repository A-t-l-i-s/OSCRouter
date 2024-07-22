from engine.require import *

from .client import *





__all__ = ("OSCServer", "OSCServer_Client")





class OSCServer(RFT_Object):
	# ~~~~~~~~~~ Initialize ~~~~~~~~~~
	def __init__(self, ip:str, port:int):
		# ~~~~~~~ Variables ~~~~~~
		self.ip = ip
		self.port = port

		self.running = True
		self.logging = False

		self.clients = []
		# ~~~~~~~~~~~~~~~~~~~~~~~~


		# Dispatcher
		self.dispatcher = OSC_Dispatcher()
		self.dispatcher.set_default_handler(self.default)


		# Server
		self.server = None
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Server ~~~~~~~~~~~~
	def run(self):
		threading._start_new_thread(
			self.run_,
			(),
			{}
		)


	def run_(self):
		while self.running:
			if (self.server == None):
				try:
					# Create server
					self.server = OSC_BlockingServer(
						(
							self.ip,
							self.port
						),
						self.dispatcher
					)

				except:
					self.server = None

				else:
					# Configure server
					self.server.allow_reuse_address = True
					self.server.allow_reuse_port = True
					self.server.max_packet_size = 8192
					self.server.timeout = 3

				finally:
					# Wait
					time.sleep(1)


			else:
				try:
					# Handle server requests
					self.server.handle_request()
				except:
					...
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Clients ~~~~~~~~~~~
	def add(self, ip, port):
		# Create new client
		client = OSCServer_Client(
			ip,
			port
		)

		# Add client
		self.clients.append(client)


	def default(self, address:str, *values):
		if (self.logging):
			# Logging
			RFT_Exception(f"{address}: {values}").print()


		for c in self.clients:
			# Trigger client
			c.trigger(
				address,
				values
			)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


