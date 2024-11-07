from engine.require import *
from engine.oscserver import *





if (__name__ == "__main__"):
	# Initialize parser
	parser = argparse.ArgumentParser(
		prog = "OSC Router",
		description = "Routes dispatching osc requests to different ports"
	)

	# Add arguments
	parser.add_argument("-s", "--server", type = str)
	parser.add_argument("-c", "--client", type = str, action = "extend", nargs = "+")

	# Parse args
	args = parser.parse_args()


	# Parse server ip/port
	if (ser := args.server):
		try:
			# Split at comma
			ip, port = ser.split(":")

			# Set server ip/port
			Data.server.serverIp = str(ip)
			Data.server.serverPort = int(port)
		except:
			...


	# Parse clients ip/port
	if (cl := args.client):
		for c in cl:
			try:
				# Split at comma
				ip, port = c.split(":")

				# Append client to clients
				Data.server.clients.append(
					{
						"ip": str(ip),
						"port": int(port)
					}
				)
			except:
				...



	# Create server handler
	server = OSCServer(
		Data.server.serverIp,
		Data.server.serverPort
	)

	# Log trying to connect
	RFT_Exception(f"Connecting to {server.ip}:{server.port}...", 0).print()

	# Add clients
	for s in Data.server.clients:
		server.add(
			s["ip"],
			s["port"]
		)

	# Run server
	server.run()


