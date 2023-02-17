from supportedSignals import supportedSignals, classSignals
from xml.etree import ElementTree as ET
from PyQt5 import QtWidgets
import sys
import os



def showErrorAndQuit(errorMessage):
    app = QtWidgets.QApplication([])
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText(errorMessage)
    msg.show()
    app.exec_()


