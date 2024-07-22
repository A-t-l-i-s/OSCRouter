import sys
sys.path.append("/RFTLib/src")

import os
import idna
import math
import time
import yaml
import types
import random
import threading


# Python OSC
from pythonosc.dispatcher import Dispatcher as OSC_Dispatcher
from pythonosc.udp_client import SimpleUDPClient as OSC_Client
from pythonosc.osc_server import BlockingOSCUDPServer as OSC_BlockingServer

# Qt6
from PyQt6.QtGui import (
	QFontDatabase, QFontMetrics, QAction,
	QImage, QPixmap, QIcon,
	QPainter, QColor, QPen,
	QBrush, QMouseEvent, QCursor,
	QFont, QPaintEvent, QKeyEvent,
	QShortcut, QKeySequence
)

from PyQt6.QtCore import (
	Qt, QObject, pyqtSlot, QEvent, QTimer, QPoint
)

from PyQt6.QtWidgets import (
	QApplication, QMainWindow, QWidget, QMenu, QSystemTrayIcon, QStackedLayout, QLineEdit, QWidgetAction, QFileDialog, QCheckBox
)

# RFTLib
from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *
from RFTLib.Core.Exception import *

from RFTLib.Core.Table import *
from RFTLib.Core.Resource import *



# ~~~~~~~~~~~~~~ Qt ~~~~~~~~~~~~~~
qtApp = QApplication([""])

QFontDatabase.addApplicationFont("./res/fonts/Dosis-Bold.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-ExtraBold.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-ExtraLight.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Light.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Medium.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Regular.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-SemiBold.ttf")

qtApp.setStyle("Fusion")
qtApp.setFont(
	QFont("Dosis-Bold", 10)
)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~ Data ~~~~~~~~~~~~~
Data_Obj = RFT_Resource(
	"./res/data",
	{
		r"yaml": RFT_Resource_YAML,
		r"json": RFT_Resource_JSON
	}
)

Data_Obj.verify()
Data = Data_Obj.load()
Data.lift("Data")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Styles ~~~~~~~~~~~~
Styles_Obj = RFT_Resource(
	"./res/styles",
	{
		r"[cq]ss": RFT_Resource_TEXT
	}
)

Styles_Obj.verify()
Styles = Styles_Obj.load()
Styles.lift("Styles")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Images ~~~~~~~~~~~~
Images_Obj = RFT_Resource(
	"./res/images",
	{
		r"png": RFT_Resource_QT_QIMAGE
	}
)

Images_Obj.verify()
Images = Images_Obj.load()
Images.lift("Images")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~ Icons ~~~~~~~~~~~~
Icons_Obj = RFT_Resource(
	"./res/icons",
	{
		r"png": RFT_Resource_QT_QICON
	}
)

Icons_Obj.verify()
Icons = Icons_Obj.load()
Icons.lift("Icons")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Tables ~~~~~~~~~~~~
Tables_Obj = RFT_Table(
	"./res/tables"
)

Tables_Obj.verify()
Tables_Obj.saveEvery(30)

Tables = Tables_Obj.data
Tables.lift("Tables")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


