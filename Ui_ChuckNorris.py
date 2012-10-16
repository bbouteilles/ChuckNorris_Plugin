# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ChuckNorris.ui'
#
# Created: Tue Oct 16 14:13:12 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChuckNorris(object):
    def setupUi(self, ChuckNorris):
        ChuckNorris.setObjectName(_fromUtf8("ChuckNorris"))
        ChuckNorris.resize(790, 96)
        self.lbl_fact = QtGui.QLabel(ChuckNorris)
        self.lbl_fact.setGeometry(QtCore.QRect(10, 10, 761, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Garamond"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lbl_fact.setFont(font)
        self.lbl_fact.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_fact.setObjectName(_fromUtf8("lbl_fact"))

        self.retranslateUi(ChuckNorris)
        QtCore.QMetaObject.connectSlotsByName(ChuckNorris)

    def retranslateUi(self, ChuckNorris):
        ChuckNorris.setWindowTitle(QtGui.QApplication.translate("ChuckNorris", "The Chuck Norris plugin :", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_fact.setText(QtGui.QApplication.translate("ChuckNorris", "default fact", None, QtGui.QApplication.UnicodeUTF8))

