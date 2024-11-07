import sys

import idna
import time
import argparse
import threading


# Python OSC
from pythonosc.dispatcher import Dispatcher as OSC_Dispatcher
from pythonosc.udp_client import SimpleUDPClient as OSC_Client
from pythonosc.osc_server import BlockingOSCUDPServer as OSC_BlockingServer


# RFTLib
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *

from RFTLib.Core.Resource import *



# ~~~~~~~~~~~~~ Data ~~~~~~~~~~~~~
Data_Obj = RFT_Resource(
	"./data",
	{
		r"yaml": RFT_Resource_YAML
	}
)

Data = Data_Obj.load()
Data.lift("Data")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


