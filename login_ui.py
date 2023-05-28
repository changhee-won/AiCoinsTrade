# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 200)
        Dialog.setMinimumSize(QSize(400, 200))
        Dialog.setMaximumSize(QSize(400, 200))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(8)
        font.setBold(True)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_aes = QLabel(Dialog)
        self.label_aes.setObjectName(u"label_aes")
        self.label_aes.setMinimumSize(QSize(100, 30))
        self.label_aes.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(7)
        font1.setBold(True)
        self.label_aes.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_aes)

        self.lineEdit_aes = QLineEdit(Dialog)
        self.lineEdit_aes.setObjectName(u"lineEdit_aes")
        self.lineEdit_aes.setMinimumSize(QSize(200, 30))
        self.lineEdit_aes.setMaximumSize(QSize(200, 30))
        self.lineEdit_aes.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineEdit_aes)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_sec = QLabel(Dialog)
        self.label_sec.setObjectName(u"label_sec")
        self.label_sec.setMinimumSize(QSize(100, 30))
        self.label_sec.setMaximumSize(QSize(100, 30))
        self.label_sec.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_sec)

        self.lineEdit_sec = QLineEdit(Dialog)
        self.lineEdit_sec.setObjectName(u"lineEdit_sec")
        self.lineEdit_sec.setMinimumSize(QSize(200, 30))
        self.lineEdit_sec.setMaximumSize(QSize(200, 30))
        self.lineEdit_sec.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_sec)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox_save = QCheckBox(Dialog)
        self.checkBox_save.setObjectName(u"checkBox_save")
        self.checkBox_save.setFont(font)

        self.horizontalLayout.addWidget(self.checkBox_save)

        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setMinimumSize(QSize(100, 30))
        self.pushButton_ok.setMaximumSize(QSize(100, 30))
        self.pushButton_ok.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_ok)

        self.pushButton_exit = QPushButton(Dialog)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setMinimumSize(QSize(100, 30))
        self.pushButton_exit.setMaximumSize(QSize(100, 30))
        self.pushButton_exit.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_exit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.label_aes.setText(QCoreApplication.translate("Dialog", u"AES Key", None))
        self.label_sec.setText(QCoreApplication.translate("Dialog", u"Security Key", None))
        self.checkBox_save.setText(QCoreApplication.translate("Dialog", u"Save Key", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

