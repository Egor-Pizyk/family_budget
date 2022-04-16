from PyQt5 import QtCore, QtGui, QtWidgets
from v5.handler.db_handler import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)

    def thr_login(self, log, pas):
        login(log, pas, self.mysignal)

    def thr_reg(self, log, pas):
        reg(log, pas, self.mysignal)