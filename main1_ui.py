# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main1.ui'
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
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 800)
        MainWindow.setMinimumSize(QSize(200, 800))
        MainWindow.setMaximumSize(QSize(1162, 800))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(615, 0))
        self.tabWidget.setMaximumSize(QSize(615, 16777215))
        self.tabWidget.setFont(font)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.gridLayout = QGridLayout(self.tabWidgetPage1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget_2 = QTabWidget(self.tabWidgetPage1)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(600, 0))
        self.tabWidget_2.setMaximumSize(QSize(600, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(8)
        self.tabWidget_2.setFont(font1)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_limit = QRadioButton(self.tab_3)
        self.radioButton_limit.setObjectName(u"radioButton_limit")
        self.radioButton_limit.setMinimumSize(QSize(60, 30))
        self.radioButton_limit.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_5.addWidget(self.radioButton_limit)

        self.radioButton_cur = QRadioButton(self.tab_3)
        self.radioButton_cur.setObjectName(u"radioButton_cur")
        self.radioButton_cur.setMinimumSize(QSize(60, 30))
        self.radioButton_cur.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_5.addWidget(self.radioButton_cur)

        self.radioButton_reserve = QRadioButton(self.tab_3)
        self.radioButton_reserve.setObjectName(u"radioButton_reserve")
        self.radioButton_reserve.setMinimumSize(QSize(60, 30))
        self.radioButton_reserve.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_5.addWidget(self.radioButton_reserve)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 30))
        self.label_4.setMaximumSize(QSize(80, 30))
        self.label_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.doubleSpinBox_amt = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_amt.setObjectName(u"doubleSpinBox_amt")
        self.doubleSpinBox_amt.setMinimumSize(QSize(200, 30))
        self.doubleSpinBox_amt.setMaximumSize(QSize(200, 30))
        self.doubleSpinBox_amt.setFont(font)
        self.doubleSpinBox_amt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_amt)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 30))
        self.label_3.setMaximumSize(QSize(40, 30))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.comboBox_buyratio_1 = QComboBox(self.tab_3)
        self.comboBox_buyratio_1.setObjectName(u"comboBox_buyratio_1")
        self.comboBox_buyratio_1.setMinimumSize(QSize(50, 30))
        self.comboBox_buyratio_1.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_6.addWidget(self.comboBox_buyratio_1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 30))
        self.label_2.setMaximumSize(QSize(20, 30))

        self.horizontalLayout_6.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 30))
        self.label_7.setMaximumSize(QSize(80, 30))
        self.label_7.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.doubleSpinBox = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(200, 30))
        self.doubleSpinBox.setMaximumSize(QSize(200, 30))
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.doubleSpinBox)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 30))
        self.label_6.setMaximumSize(QSize(40, 30))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.comboBox_buyratio = QComboBox(self.tab_3)
        self.comboBox_buyratio.setObjectName(u"comboBox_buyratio")
        self.comboBox_buyratio.setMinimumSize(QSize(50, 30))
        self.comboBox_buyratio.setMaximumSize(QSize(50, 30))
        self.comboBox_buyratio.setFont(font)
        self.comboBox_buyratio.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_buyratio.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_8.addWidget(self.comboBox_buyratio)

        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(20, 30))
        self.label_11.setMaximumSize(QSize(20, 30))
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 30))
        self.label_9.setMaximumSize(QSize(80, 30))
        self.label_9.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.doubleSpinBox_tprice = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_tprice.setObjectName(u"doubleSpinBox_tprice")
        self.doubleSpinBox_tprice.setMinimumSize(QSize(200, 30))
        self.doubleSpinBox_tprice.setMaximumSize(QSize(200, 30))
        self.doubleSpinBox_tprice.setFont(font)
        self.doubleSpinBox_tprice.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_tprice)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(170, 30))
        self.label_10.setMaximumSize(QSize(170, 30))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.pushButton_init = QPushButton(self.tab_3)
        self.pushButton_init.setObjectName(u"pushButton_init")
        self.pushButton_init.setMinimumSize(QSize(150, 30))
        self.pushButton_init.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_init)

        self.pushButton_buy = QPushButton(self.tab_3)
        self.pushButton_buy.setObjectName(u"pushButton_buy")
        self.pushButton_buy.setMinimumSize(QSize(150, 30))
        self.pushButton_buy.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_buy)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_3 = QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_slimit = QRadioButton(self.tab_5)
        self.radioButton_slimit.setObjectName(u"radioButton_slimit")
        self.radioButton_slimit.setMinimumSize(QSize(60, 30))
        self.radioButton_slimit.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_22.addWidget(self.radioButton_slimit)

        self.radioButton_scur = QRadioButton(self.tab_5)
        self.radioButton_scur.setObjectName(u"radioButton_scur")
        self.radioButton_scur.setMinimumSize(QSize(60, 30))
        self.radioButton_scur.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_22.addWidget(self.radioButton_scur)

        self.radioButton_sreserve = QRadioButton(self.tab_5)
        self.radioButton_sreserve.setObjectName(u"radioButton_sreserve")
        self.radioButton_sreserve.setMinimumSize(QSize(60, 30))
        self.radioButton_sreserve.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_22.addWidget(self.radioButton_sreserve)


        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_25 = QLabel(self.tab_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(80, 30))
        self.label_25.setMaximumSize(QSize(80, 30))
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_25)

        self.doubleSpinBox_sellamt = QDoubleSpinBox(self.tab_5)
        self.doubleSpinBox_sellamt.setObjectName(u"doubleSpinBox_sellamt")
        self.doubleSpinBox_sellamt.setMinimumSize(QSize(200, 30))
        self.doubleSpinBox_sellamt.setMaximumSize(QSize(200, 30))
        self.doubleSpinBox_sellamt.setFont(font)
        self.doubleSpinBox_sellamt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.doubleSpinBox_sellamt)

        self.label_26 = QLabel(self.tab_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(40, 30))
        self.label_26.setMaximumSize(QSize(40, 30))
        self.label_26.setFont(font)
        self.label_26.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_26)

        self.comboBox_sellratio_1 = QComboBox(self.tab_5)
        self.comboBox_sellratio_1.setObjectName(u"comboBox_sellratio_1")
        self.comboBox_sellratio_1.setMinimumSize(QSize(50, 30))
        self.comboBox_sellratio_1.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_18.addWidget(self.comboBox_sellratio_1)

        self.label = QLabel(self.tab_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(20, 30))
        self.label.setMaximumSize(QSize(20, 30))

        self.horizontalLayout_18.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_23 = QLabel(self.tab_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(80, 30))
        self.label_23.setMaximumSize(QSize(80, 30))
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_23)

        self.doubleSpinBox_sellprice = QDoubleSpinBox(self.tab_5)
        self.doubleSpinBox_sellprice.setObjectName(u"doubleSpinBox_sellprice")
        self.doubleSpinBox_sellprice.setMinimumSize(QSize(200, 30))
        self.doubleSpinBox_sellprice.setMaximumSize(QSize(200, 30))
        self.doubleSpinBox_sellprice.setFont(font)
        self.doubleSpinBox_sellprice.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.doubleSpinBox_sellprice)

        self.label_24 = QLabel(self.tab_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(40, 30))
        self.label_24.setMaximumSize(QSize(40, 30))
        self.label_24.setFont(font)
        self.label_24.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_24)

        self.comboBox_sellratio = QComboBox(self.tab_5)
        self.comboBox_sellratio.setObjectName(u"comboBox_sellratio")
        self.comboBox_sellratio.setMinimumSize(QSize(50, 30))
        self.comboBox_sellratio.setMaximumSize(QSize(50, 30))
        self.comboBox_sellratio.setFont(font)
        self.comboBox_sellratio.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_17.addWidget(self.comboBox_sellratio)

        self.label_12 = QLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(20, 30))
        self.label_12.setMaximumSize(QSize(20, 30))
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_19 = QLabel(self.tab_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(80, 30))
        self.label_19.setMaximumSize(QSize(80, 30))
        self.label_19.setTabletTracking(False)
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_19)

        self.doubleSpinBox_selltot = QDoubleSpinBox(self.tab_5)
        self.doubleSpinBox_selltot.setObjectName(u"doubleSpinBox_selltot")
        self.doubleSpinBox_selltot.setMinimumSize(QSize(200, 30))
        self.doubleSpinBox_selltot.setMaximumSize(QSize(200, 30))
        self.doubleSpinBox_selltot.setFont(font)
        self.doubleSpinBox_selltot.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.doubleSpinBox_selltot)

        self.label_20 = QLabel(self.tab_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(170, 30))
        self.label_20.setMaximumSize(QSize(170, 30))
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_20)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)

        self.pushButton_sellinit = QPushButton(self.tab_5)
        self.pushButton_sellinit.setObjectName(u"pushButton_sellinit")
        self.pushButton_sellinit.setMinimumSize(QSize(150, 30))
        self.pushButton_sellinit.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_19.addWidget(self.pushButton_sellinit)

        self.pushButton_sell = QPushButton(self.tab_5)
        self.pushButton_sell.setObjectName(u"pushButton_sell")
        self.pushButton_sell.setMinimumSize(QSize(150, 30))
        self.pushButton_sell.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_19.addWidget(self.pushButton_sell)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.radioButton_trade = QRadioButton(self.tab_4)
        self.radioButton_trade.setObjectName(u"radioButton_trade")
        self.radioButton_trade.setMinimumSize(QSize(60, 30))
        self.radioButton_trade.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_23.addWidget(self.radioButton_trade)

        self.radioButton_notrade = QRadioButton(self.tab_4)
        self.radioButton_notrade.setObjectName(u"radioButton_notrade")
        self.radioButton_notrade.setMinimumSize(QSize(60, 30))
        self.radioButton_notrade.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_23.addWidget(self.radioButton_notrade)


        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.tableWidget_tradelist = QTableWidget(self.tab_4)
        if (self.tableWidget_tradelist.columnCount() < 8):
            self.tableWidget_tradelist.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_tradelist.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_tradelist.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_tradelist.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_tradelist.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_tradelist.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_tradelist.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_tradelist.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_tradelist.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget_tradelist.setObjectName(u"tableWidget_tradelist")
        self.tableWidget_tradelist.setMinimumSize(QSize(0, 0))
        self.tableWidget_tradelist.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_tradelist.setFont(font)
        self.tableWidget_tradelist.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.tableWidget_tradelist)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_5.addWidget(self.tabWidget_2)

        self.tableWidget_tot = QTableWidget(self.tabWidgetPage1)
        if (self.tableWidget_tot.columnCount() < 5):
            self.tableWidget_tot.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font1);
        self.tableWidget_tot.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font1);
        self.tableWidget_tot.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font1);
        self.tableWidget_tot.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font1);
        self.tableWidget_tot.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font1);
        self.tableWidget_tot.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.tableWidget_tot.setObjectName(u"tableWidget_tot")
        self.tableWidget_tot.setMinimumSize(QSize(0, 200))
        self.tableWidget_tot.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_tot.setFont(font)
        self.tableWidget_tot.horizontalHeader().setVisible(False)
        self.tableWidget_tot.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_tot.horizontalHeader().setStretchLastSection(False)
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

        self.label_market = QLabel(self.tabWidgetPage2)
        self.label_market.setObjectName(u"label_market")
        self.label_market.setMinimumSize(QSize(0, 30))
        self.label_market.setMaximumSize(QSize(16777215, 30))
        self.label_market.setFont(font1)
        self.label_market.setFrameShape(QFrame.Box)
        self.label_market.setFrameShadow(QFrame.Sunken)
        self.label_market.setLineWidth(2)
        self.label_market.setMidLineWidth(1)
        self.label_market.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_market)

        self.tableWidget_tradesum = QTableWidget(self.tabWidgetPage2)
        if (self.tableWidget_tradesum.columnCount() < 7):
            self.tableWidget_tradesum.setColumnCount(7)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font1);
        self.tableWidget_tradesum.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font1);
        self.tableWidget_tradesum.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font1);
        self.tableWidget_tradesum.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font1);
        self.tableWidget_tradesum.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font1);
        self.tableWidget_tradesum.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font1);
        self.tableWidget_tradesum.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font1);
        self.tableWidget_tradesum.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        self.tableWidget_tradesum.setObjectName(u"tableWidget_tradesum")
        self.tableWidget_tradesum.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableWidget_tradesum)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_add = QPushButton(self.tab)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMinimumSize(QSize(20, 85))
        self.pushButton_add.setMaximumSize(QSize(20, 85))

        self.verticalLayout_7.addWidget(self.pushButton_add)

        self.pushButton_remove = QPushButton(self.tab)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setMinimumSize(QSize(20, 85))
        self.pushButton_remove.setMaximumSize(QSize(20, 85))

        self.verticalLayout_7.addWidget(self.pushButton_remove)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.treeWidget_autolist = QTreeWidget(self.tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_autolist.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_autolist.setObjectName(u"treeWidget_autolist")

        self.horizontalLayout_3.addWidget(self.treeWidget_autolist)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 150))
        self.groupBox.setMaximumSize(QSize(16777215, 150))
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(60, 30))
        self.label_15.setMaximumSize(QSize(60, 30))
        self.label_15.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_15)

        self.comboBox_asellrate = QComboBox(self.groupBox)
        self.comboBox_asellrate.setObjectName(u"comboBox_asellrate")
        self.comboBox_asellrate.setMinimumSize(QSize(100, 30))
        self.comboBox_asellrate.setMaximumSize(QSize(100, 30))
        self.comboBox_asellrate.setEditable(False)

        self.horizontalLayout_12.addWidget(self.comboBox_asellrate)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(60, 30))
        self.label_14.setMaximumSize(QSize(60, 30))
        self.label_14.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.doubleSpinBox_asellprice = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_asellprice.setObjectName(u"doubleSpinBox_asellprice")
        self.doubleSpinBox_asellprice.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_asellprice.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_asellprice.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.doubleSpinBox_asellprice)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(60, 30))
        self.label_27.setMaximumSize(QSize(60, 30))
        self.label_27.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

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
        self.label_28.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_28)

        self.doubleSpinBox_asellamt = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_asellamt.setObjectName(u"doubleSpinBox_asellamt")
        self.doubleSpinBox_asellamt.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_asellamt.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_asellamt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.doubleSpinBox_asellamt)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)


        self.verticalLayout_10.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 150))
        self.groupBox_2.setMaximumSize(QSize(16777215, 150))
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(60, 30))
        self.label_13.setMaximumSize(QSize(60, 30))
        self.label_13.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_13)

        self.comboBox_abuyrate = QComboBox(self.groupBox_2)
        self.comboBox_abuyrate.setObjectName(u"comboBox_abuyrate")
        self.comboBox_abuyrate.setMinimumSize(QSize(100, 30))
        self.comboBox_abuyrate.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_24.addWidget(self.comboBox_abuyrate)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(60, 30))
        self.label_16.setMaximumSize(QSize(60, 30))
        self.label_16.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_16)

        self.doubleSpinBox_abuyprice = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_abuyprice.setObjectName(u"doubleSpinBox_abuyprice")
        self.doubleSpinBox_abuyprice.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_abuyprice.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_abuyprice.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.doubleSpinBox_abuyprice)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_30 = QLabel(self.groupBox_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(60, 30))
        self.label_30.setMaximumSize(QSize(60, 30))
        self.label_30.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_30)

        self.comboBox_aspbuyrate = QComboBox(self.groupBox_2)
        self.comboBox_aspbuyrate.setObjectName(u"comboBox_aspbuyrate")
        self.comboBox_aspbuyrate.setMinimumSize(QSize(100, 30))
        self.comboBox_aspbuyrate.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_25.addWidget(self.comboBox_aspbuyrate)

        self.label_31 = QLabel(self.groupBox_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(60, 30))
        self.label_31.setMaximumSize(QSize(60, 30))
        self.label_31.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_31)

        self.doubleSpinBox_abuyamt = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_abuyamt.setObjectName(u"doubleSpinBox_abuyamt")
        self.doubleSpinBox_abuyamt.setMinimumSize(QSize(150, 30))
        self.doubleSpinBox_abuyamt.setMaximumSize(QSize(150, 30))
        self.doubleSpinBox_abuyamt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_abuyamt)


        self.verticalLayout_9.addLayout(self.horizontalLayout_25)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 150))
        self.groupBox_3.setMaximumSize(QSize(16777215, 150))
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_ma = QLabel(self.groupBox_3)
        self.label_ma.setObjectName(u"label_ma")
        self.label_ma.setMinimumSize(QSize(80, 30))
        self.label_ma.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_21.addWidget(self.label_ma)

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
        self.label_startdate.setMinimumSize(QSize(50, 30))
        self.label_startdate.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_20.addWidget(self.label_startdate)

        self.dateTimeEdit_astart = QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit_astart.setObjectName(u"dateTimeEdit_astart")
        self.dateTimeEdit_astart.setMinimumSize(QSize(200, 30))
        self.dateTimeEdit_astart.setMaximumSize(QSize(200, 30))
        self.dateTimeEdit_astart.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.dateTimeEdit_astart)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.label_enddate = QLabel(self.groupBox_3)
        self.label_enddate.setObjectName(u"label_enddate")
        self.label_enddate.setMinimumSize(QSize(50, 30))
        self.label_enddate.setMaximumSize(QSize(50, 30))

        self.horizontalLayout_13.addWidget(self.label_enddate)

        self.dateTimeEdit_aend = QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit_aend.setObjectName(u"dateTimeEdit_aend")
        self.dateTimeEdit_aend.setMinimumSize(QSize(200, 30))
        self.dateTimeEdit_aend.setMaximumSize(QSize(200, 30))
        self.dateTimeEdit_aend.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.dateTimeEdit_aend)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)


        self.verticalLayout_10.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 2, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(110, 30))
        self.pushButton_close.setMaximumSize(QSize(150, 30))

        self.gridLayout_3.addWidget(self.pushButton_close, 0, 3, 1, 1)

        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(110, 30))
        self.pushButton_stop.setMaximumSize(QSize(150, 30))

        self.gridLayout_3.addWidget(self.pushButton_stop, 0, 2, 1, 1)

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(110, 30))
        self.pushButton_start.setMaximumSize(QSize(150, 30))

        self.gridLayout_3.addWidget(self.pushButton_start, 0, 1, 1, 1)

        self.pushButton_reflash = QPushButton(self.centralwidget)
        self.pushButton_reflash.setObjectName(u"pushButton_reflash")
        self.pushButton_reflash.setMinimumSize(QSize(110, 30))
        self.pushButton_reflash.setMaximumSize(QSize(150, 30))

        self.gridLayout_3.addWidget(self.pushButton_reflash, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_krw = QRadioButton(self.centralwidget)
        self.radioButton_krw.setObjectName(u"radioButton_krw")
        self.radioButton_krw.setMinimumSize(QSize(60, 30))
        self.radioButton_krw.setMaximumSize(QSize(60, 30))
        self.radioButton_krw.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_krw)

        self.radioButton_fav = QRadioButton(self.centralwidget)
        self.radioButton_fav.setObjectName(u"radioButton_fav")
        self.radioButton_fav.setMinimumSize(QSize(60, 30))
        self.radioButton_fav.setMaximumSize(QSize(60, 30))

        self.horizontalLayout.addWidget(self.radioButton_fav)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tableWidget_status = QTableWidget(self.centralwidget)
        if (self.tableWidget_status.columnCount() < 4):
            self.tableWidget_status.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font1);
        self.tableWidget_status.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font1);
        self.tableWidget_status.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font1);
        self.tableWidget_status.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font1);
        self.tableWidget_status.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        self.tableWidget_status.setObjectName(u"tableWidget_status")
        self.tableWidget_status.setMinimumSize(QSize(430, 0))
        self.tableWidget_status.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_status.setFont(font)
        self.tableWidget_status.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tableWidget_status, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1076, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.comboBox_abuyrate.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton_limit.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc815\uac00", None))
        self.radioButton_cur.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc7a5\uac00", None))
        self.radioButton_reserve.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc57d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc218\ub7c9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"KRW", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"KRW", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\ucd1d\uc561", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"KRW", None))
        self.pushButton_init.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.pushButton_buy.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\ub9e4\uc218", None))
        self.radioButton_slimit.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc815\uac00", None))
        self.radioButton_scur.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc7a5\uac00", None))
        self.radioButton_sreserve.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc57d", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\uc218\ub7c9", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"KRW", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"KRW", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\ucd1d\uc561", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"KRW", None))
        self.pushButton_sellinit.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.pushButton_sell.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\ub9e4\ub3c4", None))
        self.radioButton_trade.setText(QCoreApplication.translate("MainWindow", u"\uccb4\uacb0", None))
        self.radioButton_notrade.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\uccb4\uacb0", None))
        ___qtablewidgetitem = self.tableWidget_tradelist.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_tradelist.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04", None));
        ___qtablewidgetitem2 = self.tableWidget_tradelist.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ub9c8\ucf13", None));
        ___qtablewidgetitem3 = self.tableWidget_tradelist.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uad6c\ubd84", None));
        ___qtablewidgetitem4 = self.tableWidget_tradelist.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38\uc720\ud615", None));
        ___qtablewidgetitem5 = self.tableWidget_tradelist.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9", None));
        ___qtablewidgetitem6 = self.tableWidget_tradelist.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38\ub7c9", None));
        ___qtablewidgetitem7 = self.tableWidget_tradelist.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\uccb4\uacb0\ub7c9", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\uac70\ub798\ub0b4\uc5ed", None))
        ___qtablewidgetitem8 = self.tableWidget_tot.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\ub9c8\ucf13", None));
        ___qtablewidgetitem9 = self.tableWidget_tot.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\uc218\uac00", None));
        ___qtablewidgetitem10 = self.tableWidget_tot.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\uc794\uace0", None));
        ___qtablewidgetitem11 = self.tableWidget_tot.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem12 = self.tableWidget_tot.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc775\uc728", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("MainWindow", u"\uc794\uace0", None))
        self.label_market.setText("")
        ___qtablewidgetitem13 = self.tableWidget_tradesum.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04", None));
        ___qtablewidgetitem14 = self.tableWidget_tradesum.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\uac70\ub798\uae08\uc561", None));
        ___qtablewidgetitem15 = self.tableWidget_tradesum.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\uac70\ub798\ub7c9", None));
        ___qtablewidgetitem16 = self.tableWidget_tradesum.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\uc804\uc77c\uc885\uac00", None));
        ___qtablewidgetitem17 = self.tableWidget_tradesum.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\ubcc0\ub3d9\uac00\uaca9", None));
        ___qtablewidgetitem18 = self.tableWidget_tradesum.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\uad6c\ubd84", None));
        ___qtablewidgetitem19 = self.tableWidget_tradesum.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4\ud604\ud669", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_remove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\ub9e4\ub3c4 \ubaa9\ud45c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\ube44\uc728", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ud560\ube44\uc728", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\uc218\ub7c9", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\ub9e4\uc218 \ubaa9\ud45c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\ube44\uc728", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ud560\ube44\uc728", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\uc218\ub7c9", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u" \uae30\uc900\uc77c", None))
        self.label_ma.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub3d9 \ud3c9\uade0 ", None))
        self.radioButton_mam.setText(QCoreApplication.translate("MainWindow", u"\uc6d4", None))
        self.radioButton_maw.setText(QCoreApplication.translate("MainWindow", u"\uc8fc", None))
        self.radioButton_mad.setText(QCoreApplication.translate("MainWindow", u"\uc77c", None))
        self.label_startdate.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\uc77c", None))
        self.label_enddate.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc\uc77c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uc790\ub3d9 \ub9e4\ub9e4 \uc124\uc815", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub3d9 \ub9e4\ub9e4 \uc911\uc9c0", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub3d9 \ub9e4\ub9e4 \uc2dc\uc791", None))
        self.pushButton_reflash.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc2dc \ubd88\ub7ec\uc624\uae30", None))
        self.radioButton_krw.setText(QCoreApplication.translate("MainWindow", u"KRW", None))
        self.radioButton_fav.setText(QCoreApplication.translate("MainWindow", u"\uad00\uc2ec", None))
        ___qtablewidgetitem20 = self.tableWidget_status.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\ub9c8\ucf13", None));
        ___qtablewidgetitem21 = self.tableWidget_status.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\uc218\ub7c9", None));
        ___qtablewidgetitem22 = self.tableWidget_status.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));
        ___qtablewidgetitem23 = self.tableWidget_status.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\ub4f1\ub77d\uc728", None));
    # retranslateUi

