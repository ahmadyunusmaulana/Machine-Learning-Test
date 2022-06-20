import time
import platform, subprocess, os
import numpy as np
import os
import sys
import json
import csv
from csv import DictWriter
import pandas as pd

from datetime import date
from datetime import datetime


from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QScrollBar,QSplitter,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog, QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit
from PyQt5.QtCore import pyqtSlot, QSettings, QTimer, QUrl, QDir
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication

from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                          QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                         QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5 import uic

counter_up = 0


class Q2_Inspection(QDialog):
	def __init__(self):
		super(Q2_Inspection, self).__init__()
		loadUi('form.ui', self)
		

	def open_file(self):
		self.dir_ = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', '', QtWidgets.QFileDialog.ShowDirsOnly)
		self.folder_program_location.setText(str(self.dir_))
		self.folder_solution_location.setText(str(self.dir_))
		self.folder_api_location.setText(str(self.dir_))

	def save_api_param(self):
		self.dir_ = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', '', QtWidgets.QFileDialog.ShowDirsOnly)
		self.save_api.setText(str(self.dir_))
		pass
		

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Q2_Inspection()
	window.setWindowTitle('Q2 Decission Apps')
	window.show()
	sys.exit(app.exec_())