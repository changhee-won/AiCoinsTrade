# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1182, 725)
        self.formLayout = QFormLayout(Widget)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.treeWidget_coins = QTreeWidget(Widget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget_coins.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_coins.setObjectName(u"treeWidget_coins")
        self.treeWidget_coins.setMinimumSize(QSize(200, 0))
        self.treeWidget_coins.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.treeWidget_coins)

        self.tableWidget_status = QTableWidget(Widget)
        if (self.tableWidget_status.columnCount() < 4):
            self.tableWidget_status.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_status.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_status.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_status.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_status.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_status.setObjectName(u"tableWidget_status")
        self.tableWidget_status.setMinimumSize(QSize(430, 0))
        self.tableWidget_status.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_status.verticalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.tableWidget_status)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_4)

        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(500, 0))
        self.tabWidget.setMaximumSize(QSize(500, 16777215))
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.gridLayout = QGridLayout(self.tabWidgetPage1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget_2 = QTabWidget(self.tabWidgetPage1)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(150, 0))
        self.tabWidget_2.setMaximumSize(QSize(500, 16777215))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_2 = QRadioButton(self.tab_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(60, 30))
        self.radioButton_2.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_5.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.tab_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(60, 30))
        self.radioButton.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_5.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.tab_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(60, 30))
        self.radioButton_3.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_5.addWidget(self.radioButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 30))
        self.label.setMaximumSize(QSize(80, 30))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 30))
        self.label_4.setMaximumSize(QSize(80, 30))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.label_KRW = QLabel(self.tab_3)
        self.label_KRW.setObjectName(u"label_KRW")
        self.label_KRW.setMinimumSize(QSize(200, 30))
        self.label_KRW.setMaximumSize(QSize(200, 30))
        self.label_KRW.setFrameShape(QFrame.Box)
        self.label_KRW.setFrameShadow(QFrame.Raised)
        self.label_KRW.setLineWidth(1)
        self.label_KRW.setMidLineWidth(2)
        self.label_KRW.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_KRW)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 30))
        self.label_3.setMaximumSize(QSize(40, 30))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 30))
        self.label_7.setMaximumSize(QSize(80, 30))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(200, 30))
        self.spinBox.setMaximumSize(QSize(200, 30))
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.spinBox)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 30))
        self.label_6.setMaximumSize(QSize(40, 30))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 30))
        self.label_8.setMaximumSize(QSize(80, 30))
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.comboBox = QComboBox(self.tab_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 30))
        self.comboBox.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_9.addWidget(self.comboBox)

        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(30, 30))
        self.label_11.setMaximumSize(QSize(30, 30))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 30))
        self.label_9.setMaximumSize(QSize(80, 30))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.spinBox_3 = QSpinBox(self.tab_3)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(200, 30))
        self.spinBox_3.setMaximumSize(QSize(200, 30))
        self.spinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.spinBox_3)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 30))
        self.label_10.setMaximumSize(QSize(30, 30))
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tab_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_3 = QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_4 = QRadioButton(self.tab_5)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMinimumSize(QSize(60, 30))
        self.radioButton_4.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_22.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.tab_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setMinimumSize(QSize(60, 30))
        self.radioButton_5.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_22.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.tab_5)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setMinimumSize(QSize(60, 30))
        self.radioButton_6.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_22.addWidget(self.radioButton_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(80, 30))
        self.label_29.setMaximumSize(QSize(80, 30))
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_29)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_25 = QLabel(self.tab_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(80, 30))
        self.label_25.setMaximumSize(QSize(80, 30))
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_25)

        self.label_KRW_2 = QLabel(self.tab_5)
        self.label_KRW_2.setObjectName(u"label_KRW_2")
        self.label_KRW_2.setMinimumSize(QSize(200, 30))
        self.label_KRW_2.setMaximumSize(QSize(200, 30))
        self.label_KRW_2.setFrameShape(QFrame.Box)
        self.label_KRW_2.setFrameShadow(QFrame.Raised)
        self.label_KRW_2.setLineWidth(1)
        self.label_KRW_2.setMidLineWidth(2)
        self.label_KRW_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_KRW_2)

        self.label_26 = QLabel(self.tab_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(40, 30))
        self.label_26.setMaximumSize(QSize(40, 30))
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_26)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_23 = QLabel(self.tab_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(80, 30))
        self.label_23.setMaximumSize(QSize(80, 30))
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_23)

        self.spinBox_5 = QSpinBox(self.tab_5)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMinimumSize(QSize(200, 30))
        self.spinBox_5.setMaximumSize(QSize(200, 30))
        self.spinBox_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.spinBox_5)

        self.label_24 = QLabel(self.tab_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(40, 30))
        self.label_24.setMaximumSize(QSize(40, 30))
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_24)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_18 = QLabel(self.tab_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(80, 30))
        self.label_18.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_14.addWidget(self.label_18)

        self.comboBox_2 = QComboBox(self.tab_5)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(200, 30))
        self.comboBox_2.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_14.addWidget(self.comboBox_2)

        self.label_12 = QLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(30, 30))
        self.label_12.setMaximumSize(QSize(30, 30))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_19 = QLabel(self.tab_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(80, 30))
        self.label_19.setMaximumSize(QSize(80, 30))
        self.label_19.setTabletTracking(False)
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_19)

        self.spinBox_4 = QSpinBox(self.tab_5)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimumSize(QSize(200, 30))
        self.spinBox_4.setMaximumSize(QSize(200, 30))
        self.spinBox_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.spinBox_4)

        self.label_20 = QLabel(self.tab_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(30, 30))
        self.label_20.setMaximumSize(QSize(30, 30))
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_20)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_3 = QPushButton(self.tab_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(150, 30))
        self.pushButton_3.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_19.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.tab_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(150, 30))
        self.pushButton_4.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_19.addWidget(self.pushButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.radioButton_reflash_2 = QRadioButton(self.tab_4)
        self.radioButton_reflash_2.setObjectName(u"radioButton_reflash_2")
        self.radioButton_reflash_2.setMinimumSize(QSize(60, 30))
        self.radioButton_reflash_2.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_23.addWidget(self.radioButton_reflash_2)

        self.radioButton_reflash_3 = QRadioButton(self.tab_4)
        self.radioButton_reflash_3.setObjectName(u"radioButton_reflash_3")
        self.radioButton_reflash_3.setMinimumSize(QSize(60, 30))
        self.radioButton_reflash_3.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_23.addWidget(self.radioButton_reflash_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.tableWidget = QTableWidget(self.tab_4)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_5.addWidget(self.tabWidget_2)

        self.tableWidget_tot = QTableWidget(self.tabWidgetPage1)
        if (self.tableWidget_tot.columnCount() < 5):
            self.tableWidget_tot.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_tot.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_tot.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_tot.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_tot.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_tot.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.tableWidget_tot.setObjectName(u"tableWidget_tot")
        self.tableWidget_tot.setMinimumSize(QSize(400, 0))
        self.tableWidget_tot.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_tot.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.tableWidget_tot)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.tableWidget_asksum = QTableWidget(self.tabWidgetPage2)
        if (self.tableWidget_asksum.columnCount() < 3):
            self.tableWidget_asksum.setColumnCount(3)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_asksum.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_asksum.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_asksum.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        self.tableWidget_asksum.setObjectName(u"tableWidget_asksum")

        self.verticalLayout.addWidget(self.tableWidget_asksum)

        self.tableWidget_ask = QTableWidget(self.tabWidgetPage2)
        if (self.tableWidget_ask.columnCount() < 4):
            self.tableWidget_ask.setColumnCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ask.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ask.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ask.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ask.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        self.tableWidget_ask.setObjectName(u"tableWidget_ask")
        self.tableWidget_ask.setMinimumSize(QSize(400, 0))
        self.tableWidget_ask.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_ask.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableWidget_ask)

        self.tableWidget_trade = QTableWidget(self.tabWidgetPage2)
        if (self.tableWidget_trade.columnCount() < 5):
            self.tableWidget_trade.setColumnCount(5)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_trade.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_trade.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_trade.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_trade.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_trade.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        self.tableWidget_trade.setObjectName(u"tableWidget_trade")

        self.verticalLayout.addWidget(self.tableWidget_trade)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.tabWidgetPage2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 40))
        self.label_2.setMaximumSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox_orice = QSpinBox(self.tabWidgetPage2)
        self.spinBox_orice.setObjectName(u"spinBox_orice")
        self.spinBox_orice.setMinimumSize(QSize(100, 30))
        self.spinBox_orice.setMaximumSize(QSize(150, 30))

        self.horizontalLayout.addWidget(self.spinBox_orice)

        self.label_5 = QLabel(self.tabWidgetPage2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox_pratio = QComboBox(self.tabWidgetPage2)
        self.comboBox_pratio.setObjectName(u"comboBox_pratio")
        self.comboBox_pratio.setMinimumSize(QSize(50, 30))
        self.comboBox_pratio.setMaximumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.comboBox_pratio)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_amount = QLabel(self.tabWidgetPage2)
        self.label_amount.setObjectName(u"label_amount")
        self.label_amount.setMinimumSize(QSize(50, 40))
        self.label_amount.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.label_amount)

        self.spinBox_2 = QSpinBox(self.tabWidgetPage2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(100, 30))
        self.spinBox_2.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_2.addWidget(self.spinBox_2)

        self.label_aratio = QLabel(self.tabWidgetPage2)
        self.label_aratio.setObjectName(u"label_aratio")
        self.label_aratio.setMinimumSize(QSize(40, 40))
        self.label_aratio.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_2.addWidget(self.label_aratio)

        self.comboBox_aratio = QComboBox(self.tabWidgetPage2)
        self.comboBox_aratio.setObjectName(u"comboBox_aratio")
        self.comboBox_aratio.setMinimumSize(QSize(50, 30))
        self.comboBox_aratio.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_2.addWidget(self.comboBox_aratio)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_sellcur = QPushButton(self.tabWidgetPage2)
        self.pushButton_sellcur.setObjectName(u"pushButton_sellcur")
        self.pushButton_sellcur.setMinimumSize(QSize(120, 30))
        self.pushButton_sellcur.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_sellcur)

        self.pushButton_selllimit = QPushButton(self.tabWidgetPage2)
        self.pushButton_selllimit.setObjectName(u"pushButton_selllimit")
        self.pushButton_selllimit.setMinimumSize(QSize(120, 30))
        self.pushButton_selllimit.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_selllimit)

        self.pushButton_sellall = QPushButton(self.tabWidgetPage2)
        self.pushButton_sellall.setObjectName(u"pushButton_sellall")
        self.pushButton_sellall.setMinimumSize(QSize(120, 30))
        self.pushButton_sellall.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_sellall)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 150))
        self.listWidget.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_7.addWidget(self.listWidget)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 150))
        self.groupBox.setMaximumSize(QSize(16777215, 150))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(60, 30))
        self.label_15.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_12.addWidget(self.label_15)

        self.comboBox_sellrate = QComboBox(self.groupBox)
        self.comboBox_sellrate.setObjectName(u"comboBox_sellrate")
        self.comboBox_sellrate.setMinimumSize(QSize(100, 30))
        self.comboBox_sellrate.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_12.addWidget(self.comboBox_sellrate)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(60, 30))
        self.label_14.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_12.addWidget(self.label_14)

        self.doubleSpinBox_sellprice = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_sellprice.setObjectName(u"doubleSpinBox_sellprice")
        self.doubleSpinBox_sellprice.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_sellprice.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_sellprice)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(60, 30))
        self.label_27.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_16.addWidget(self.label_27)

        self.comboBox_spsellrate = QComboBox(self.groupBox)
        self.comboBox_spsellrate.setObjectName(u"comboBox_spsellrate")
        self.comboBox_spsellrate.setMinimumSize(QSize(100, 30))
        self.comboBox_spsellrate.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_16.addWidget(self.comboBox_spsellrate)

        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(60, 30))
        self.label_28.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_16.addWidget(self.label_28)

        self.doubleSpinBox_sellamt = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_sellamt.setObjectName(u"doubleSpinBox_sellamt")
        self.doubleSpinBox_sellamt.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_sellamt.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_sellamt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.doubleSpinBox_sellamt)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 150))
        self.groupBox_2.setMaximumSize(QSize(16777215, 150))
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(60, 30))
        self.label_13.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_24.addWidget(self.label_13)

        self.comboBox_buyrate = QComboBox(self.groupBox_2)
        self.comboBox_buyrate.setObjectName(u"comboBox_buyrate")
        self.comboBox_buyrate.setMinimumSize(QSize(100, 30))
        self.comboBox_buyrate.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_24.addWidget(self.comboBox_buyrate)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(60, 30))
        self.label_16.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_24.addWidget(self.label_16)

        self.doubleSpinBox_buyprice = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_buyprice.setObjectName(u"doubleSpinBox_buyprice")
        self.doubleSpinBox_buyprice.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_buyprice.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_buyprice.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.doubleSpinBox_buyprice)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(60, 30))
        self.label_30.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_25.addWidget(self.label_30)

        self.comboBox_spbuyrate = QComboBox(self.groupBox_2)
        self.comboBox_spbuyrate.setObjectName(u"comboBox_spbuyrate")
        self.comboBox_spbuyrate.setMinimumSize(QSize(100, 30))
        self.comboBox_spbuyrate.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_25.addWidget(self.comboBox_spbuyrate)

        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(60, 30))
        self.label_31.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_25.addWidget(self.label_31)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_3.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 150))
        self.groupBox_3.setMaximumSize(QSize(16777215, 150))
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(15, 30))
        self.label_17.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_21.addWidget(self.label_17)

        self.radioButton_mam = QRadioButton(self.groupBox_3)
        self.radioButton_mam.setObjectName(u"radioButton_mam")
        self.radioButton_mam.setMinimumSize(QSize(35, 30))
        self.radioButton_mam.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_21.addWidget(self.radioButton_mam)

        self.radioButton_maw = QRadioButton(self.groupBox_3)
        self.radioButton_maw.setObjectName(u"radioButton_maw")
        self.radioButton_maw.setMinimumSize(QSize(35, 30))
        self.radioButton_maw.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_21.addWidget(self.radioButton_maw)

        self.radioButton_mad = QRadioButton(self.groupBox_3)
        self.radioButton_mad.setObjectName(u"radioButton_mad")
        self.radioButton_mad.setMinimumSize(QSize(35, 30))
        self.radioButton_mad.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_21.addWidget(self.radioButton_mad)

        self.spinBox_ma = QSpinBox(self.groupBox_3)
        self.spinBox_ma.setObjectName(u"spinBox_ma")
        self.spinBox_ma.setMinimumSize(QSize(200, 30))
        self.spinBox_ma.setMaximumSize(QSize(200, 30))
        self.spinBox_ma.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.spinBox_ma)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.label_startdate = QLabel(self.groupBox_3)
        self.label_startdate.setObjectName(u"label_startdate")
        self.label_startdate.setMinimumSize(QSize(120, 30))
        self.label_startdate.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_20.addWidget(self.label_startdate)

        self.dateTimeEdit_2 = QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setMinimumSize(QSize(200, 30))
        self.dateTimeEdit_2.setMaximumSize(QSize(200, 30))
        self.dateTimeEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.dateTimeEdit_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.label_enddate = QLabel(self.groupBox_3)
        self.label_enddate.setObjectName(u"label_enddate")
        self.label_enddate.setMinimumSize(QSize(120, 30))
        self.label_enddate.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_13.addWidget(self.label_enddate)

        self.dateTimeEdit = QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QSize(200, 30))
        self.dateTimeEdit.setMaximumSize(QSize(200, 30))
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.dateTimeEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab, "")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.tabWidget)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_close = QPushButton(Widget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(100, 30))
        self.pushButton_close.setMaximumSize(QSize(100, 30))

        self.gridLayout_3.addWidget(self.pushButton_close, 0, 3, 1, 1)

        self.pushButton_stop = QPushButton(Widget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(100, 30))
        self.pushButton_stop.setMaximumSize(QSize(100, 30))

        self.gridLayout_3.addWidget(self.pushButton_stop, 0, 2, 1, 1)

        self.pushButton_start = QPushButton(Widget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(100, 30))
        self.pushButton_start.setMaximumSize(QSize(100, 30))

        self.gridLayout_3.addWidget(self.pushButton_start, 0, 1, 1, 1)

        self.pushButton_reflash = QPushButton(Widget)
        self.pushButton_reflash.setObjectName(u"pushButton_reflash")
        self.pushButton_reflash.setMinimumSize(QSize(100, 30))
        self.pushButton_reflash.setMaximumSize(QSize(100, 30))

        self.gridLayout_3.addWidget(self.pushButton_reflash, 0, 0, 1, 1)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.gridLayout_3)

        self.lcdNumber_time = QLCDNumber(Widget)
        self.lcdNumber_time.setObjectName(u"lcdNumber_time")
        self.lcdNumber_time.setMinimumSize(QSize(200, 30))
        self.lcdNumber_time.setMaximumSize(QSize(200, 30))
        self.lcdNumber_time.setDigitCount(12)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lcdNumber_time)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        ___qtreewidgetitem = self.treeWidget_coins.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Widget", u"\ub9c8\ucf13", None));
        ___qtablewidgetitem = self.tableWidget_status.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"\ub9c8\ucf13", None));
        ___qtablewidgetitem1 = self.tableWidget_status.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"\uc218\ub7c9", None));
        ___qtablewidgetitem2 = self.tableWidget_status.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem3 = self.tableWidget_status.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"\ub4f1\ub77d\uc728", None));
        self.radioButton_2.setText(QCoreApplication.translate("Widget", u"\uc9c0\uc815\uac00", None))
        self.radioButton.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00", None))
        self.radioButton_3.setText(QCoreApplication.translate("Widget", u"\uc608\uc57d", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\uc8fc\ubb38\uac00\ub2a5", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\uc218\ub7c9", None))
        self.label_KRW.setText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"KRW", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\uac00\uaca9", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"KRW", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00 \ub300\ube44", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"%", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"\ucd1d\uc561", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"KRW", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\ucd08\uae30\ud654", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\ub9e4\uc218", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"\ub9e4\uc218", None))
        self.radioButton_4.setText(QCoreApplication.translate("Widget", u"\uc9c0\uc815\uac00", None))
        self.radioButton_5.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00", None))
        self.radioButton_6.setText(QCoreApplication.translate("Widget", u"\uc608\uc57d", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"\uc8fc\ubb38\uac00\ub2a5", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"\uc218\ub7c9", None))
        self.label_KRW_2.setText("")
        self.label_26.setText(QCoreApplication.translate("Widget", u"KRW", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"\uac00\uaca9", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"KRW", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00 \ub300\ube44", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"%", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"\ucd1d\uc561", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"KRW", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\ucd08\uae30\ud654", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"\ub9e4\uc218", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Widget", u"\ub9e4\ub3c4", None))
        self.radioButton_reflash_2.setText(QCoreApplication.translate("Widget", u"\uccb4\uacb0", None))
        self.radioButton_reflash_3.setText(QCoreApplication.translate("Widget", u"\ubbf8\uccb4\uacb0", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"\uad6c\ubd84", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"\ub9c8\ucf13\uba85", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget", u"\uccb4\uacb0\uac00\uaca9", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Widget", u"\ucc44\uacb0\uc218\ub7c9", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Widget", u"\uccb4\uacb0\uae08\uc561", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Widget", u"\uac70\ub798\ub0b4\uc5ed", None))
        ___qtablewidgetitem9 = self.tableWidget_tot.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Widget", u"\ub9c8\ucf13", None));
        ___qtablewidgetitem10 = self.tableWidget_tot.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Widget", u"\ub9e4\uc218\uac00", None));
        ___qtablewidgetitem11 = self.tableWidget_tot.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Widget", u"\uc794\uace0", None));
        ___qtablewidgetitem12 = self.tableWidget_tot.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem13 = self.tableWidget_tot.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Widget", u"\uc218\uc775\uc728", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("Widget", u"\uc794\uace0", None))
        ___qtablewidgetitem14 = self.tableWidget_asksum.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Widget", u"\uc2dc\uac04", None));
        ___qtablewidgetitem15 = self.tableWidget_asksum.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Widget", u"\ub9e4\uc218\ub7c9", None));
        ___qtablewidgetitem16 = self.tableWidget_asksum.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Widget", u"\ub9e4\ub3c4\ub7c9", None));
        ___qtablewidgetitem17 = self.tableWidget_ask.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Widget", u"\ub9e4\uc218\ud638\uac00", None));
        ___qtablewidgetitem18 = self.tableWidget_ask.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Widget", u"\ub9e4\uc218\ub7c9", None));
        ___qtablewidgetitem19 = self.tableWidget_ask.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Widget", u"\ub9e4\ub3c4\ud638\uac00", None));
        ___qtablewidgetitem20 = self.tableWidget_ask.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Widget", u"\ub9e4\ub3c4\ub7c9", None));
        ___qtablewidgetitem21 = self.tableWidget_trade.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Widget", u"\uc2dc\uac04 ", None));
        ___qtablewidgetitem22 = self.tableWidget_trade.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Widget", u"\uccb4\uacb0\uac00", None));
        ___qtablewidgetitem23 = self.tableWidget_trade.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Widget", u"\uccb4\uacb0\ub7c9", None));
        ___qtablewidgetitem24 = self.tableWidget_trade.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Widget", u"\ud589", None));
        ___qtablewidgetitem25 = self.tableWidget_trade.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Widget", u"\ub4f1\ub77d\uc728", None));
        self.label_2.setText(QCoreApplication.translate("Widget", u"\ub9e4\ub3c4\uac00", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00 \ub300\ube44", None))
        self.label_amount.setText(QCoreApplication.translate("Widget", u"\uc218\ub7c9", None))
        self.label_aratio.setText(QCoreApplication.translate("Widget", u"\ub9e4\ub3c4 \ube44\uc728", None))
        self.pushButton_sellcur.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00 \ub9e4\ub3c4", None))
        self.pushButton_selllimit.setText(QCoreApplication.translate("Widget", u"\uc9c0\uc815\uac00 \ub9e4\ub3c4", None))
        self.pushButton_sellall.setText(QCoreApplication.translate("Widget", u"\ud604\uc7ac\uac00 \uc804\ub7c9 \ub9e4\ub3c4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("Widget", u"\uc8fc\ubb38", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\ub9e4\ub3c4 \ubaa9\ud45c", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"\ube44\uc728", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"\uac00\uaca9", None))
        self.label_27.setText(QCoreApplication.translate("Widget", u"\ubd84\ud560\ube44\uc728", None))
        self.label_28.setText(QCoreApplication.translate("Widget", u"\uc218\ub7c9", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\ub9e4\uc218 \ubaa9\ud45c", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"\ube44\uc728", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"\uac00\uaca9", None))
        self.label_30.setText(QCoreApplication.translate("Widget", u"\ubd84\ud560\ube44\uc728", None))
        self.label_31.setText(QCoreApplication.translate("Widget", u"\uc218\ub7c9", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u" \uae30\uc900\uc77c", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"\uc774\ub3d9 \ud3c9\uade0 ", None))
        self.radioButton_mam.setText(QCoreApplication.translate("Widget", u"\uc6d4", None))
        self.radioButton_maw.setText(QCoreApplication.translate("Widget", u"\uc8fc", None))
        self.radioButton_mad.setText(QCoreApplication.translate("Widget", u"\uc77c", None))
        self.label_startdate.setText(QCoreApplication.translate("Widget", u"\uc2dc\uc791\uc77c", None))
        self.label_enddate.setText(QCoreApplication.translate("Widget", u"\uc885\ub8cc\uc77c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\uc790\ub3d9 \ub9e4\ub9e4 \uc124\uc815", None))
        self.pushButton_close.setText(QCoreApplication.translate("Widget", u"\uc885\ub8cc", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Widget", u"\uc790\ub3d9 \ub9e4\ub9e4 \uc911\uc9c0", None))
        self.pushButton_start.setText(QCoreApplication.translate("Widget", u"\uc790\ub3d9 \ub9e4\ub9e4 \uc2dc\uc791", None))
        self.pushButton_reflash.setText(QCoreApplication.translate("Widget", u"\ub2e4\uc2dc \ubd88\ub7ec\uc624\uae30", None))
    # retranslateUi

