# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fftabs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fftabs(object):
    def setupUi(self, fftabs):
        fftabs.setObjectName("fftabs")
        fftabs.resize(1015, 630)
        self.verticalLayout = QtWidgets.QVBoxLayout(fftabs)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(fftabs)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.linklabel = QtWidgets.QLabel(fftabs)
        self.linklabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.linklabel.setOpenExternalLinks(True)
        self.linklabel.setObjectName("linklabel")
        self.verticalLayout.addWidget(self.linklabel)

        self.retranslateUi(fftabs)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(fftabs)

    def retranslateUi(self, fftabs):
        _translate = QtCore.QCoreApplication.translate
        fftabs.setWindowTitle(_translate("fftabs", "FindFunc"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("fftabs", "Tab 1"))
        self.linklabel.setText(_translate("fftabs", "ff"))
