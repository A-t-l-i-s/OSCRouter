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

					# Log successful connection
					RFT_Exception("Successfully connected!", 0).print()

				except:
					# Log failed connection
					RFT_Exception("Failed to connect", 0).print()
					
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
				
				except KeyboardInterrupt:
					break
				
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

		# Log adding client
		RFT_Exception(f"Client dispatching to {ip}:{port}", 0).print()


	def default(self, address:str, *values):
		for c in self.clients:
			# Trigger client
			c.trigger(
				address,
				values
			)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


