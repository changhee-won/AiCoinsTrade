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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1180, 659)
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_status = QTableWidget(self.tab)
        if (self.tableWidget_status.columnCount() < 4):
            self.tableWidget_status.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_status.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_status.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_status.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_status.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_status.setObjectName(u"tableWidget_status")

        self.gridLayout.addWidget(self.tableWidget_status, 1, 1, 1, 1)

        self.spinBox_time = QSpinBox(self.tab)
        self.spinBox_time.setObjectName(u"spinBox_time")
        self.spinBox_time.setAlignment(Qt.AlignCenter)
        self.spinBox_time.setMinimum(1)
        self.spinBox_time.setMaximum(60)
        self.spinBox_time.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spinBox_time, 0, 0, 1, 1)

        self.treeWidget_coins = QTreeWidget(self.tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget_coins.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_coins.setObjectName(u"treeWidget_coins")
        self.treeWidget_coins.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.treeWidget_coins, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.formLayout = QFormLayout(self.tab_2)
        self.formLayout.setObjectName(u"formLayout")
        self.tableWidget_tot = QTableWidget(self.tab_2)
        if (self.tableWidget_tot.columnCount() < 5):
            self.tableWidget_tot.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_tot.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_tot.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_tot.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_tot.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_tot.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableWidget_tot.setObjectName(u"tableWidget_tot")
        self.tableWidget_tot.setMinimumSize(QSize(600, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.tableWidget_tot)

        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_cname = QLabel(self.groupBox)
        self.label_cname.setObjectName(u"label_cname")
        self.label_cname.setMinimumSize(QSize(100, 40))
        self.label_cname.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_4.addWidget(self.label_cname)

        self.comboBox_coins = QComboBox(self.groupBox)
        self.comboBox_coins.setObjectName(u"comboBox_coins")
        self.comboBox_coins.setMinimumSize(QSize(200, 0))
        self.comboBox_coins.setMaximumSize(QSize(200, 20))

        self.horizontalLayout_4.addWidget(self.comboBox_coins)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 40))
        self.label_2.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox_orice = QSpinBox(self.groupBox)
        self.spinBox_orice.setObjectName(u"spinBox_orice")
        self.spinBox_orice.setMinimumSize(QSize(100, 30))
        self.spinBox_orice.setMaximumSize(QSize(200, 30))

        self.horizontalLayout.addWidget(self.spinBox_orice)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 40))
        self.label_5.setMaximumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox_pratio = QComboBox(self.groupBox)
        self.comboBox_pratio.setObjectName(u"comboBox_pratio")
        self.comboBox_pratio.setMinimumSize(QSize(100, 30))
        self.comboBox_pratio.setMaximumSize(QSize(200, 30))

        self.horizontalLayout.addWidget(self.comboBox_pratio)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_amount = QLabel(self.groupBox)
        self.label_amount.setObjectName(u"label_amount")
        self.label_amount.setMinimumSize(QSize(100, 40))
        self.label_amount.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_2.addWidget(self.label_amount)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(100, 30))
        self.spinBox_2.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_2.addWidget(self.spinBox_2)

        self.label_aratio = QLabel(self.groupBox)
        self.label_aratio.setObjectName(u"label_aratio")
        self.label_aratio.setMinimumSize(QSize(100, 40))
        self.label_aratio.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_2.addWidget(self.label_aratio)

        self.comboBox_aratio = QComboBox(self.groupBox)
        self.comboBox_aratio.setObjectName(u"comboBox_aratio")
        self.comboBox_aratio.setMinimumSize(QSize(100, 30))
        self.comboBox_aratio.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_2.addWidget(self.comboBox_aratio)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_sellcur = QPushButton(self.groupBox)
        self.pushButton_sellcur.setObjectName(u"pushButton_sellcur")
        self.pushButton_sellcur.setMinimumSize(QSize(120, 30))
        self.pushButton_sellcur.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_sellcur)

        self.pushButton_selllimit = QPushButton(self.groupBox)
        self.pushButton_selllimit.setObjectName(u"pushButton_selllimit")
        self.pushButton_selllimit.setMinimumSize(QSize(120, 30))
        self.pushButton_selllimit.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_selllimit)

        self.pushButton_sellall = QPushButton(self.groupBox)
        self.pushButton_sellall.setObjectName(u"pushButton_sellall")
        self.pushButton_sellall.setMinimumSize(QSize(120, 30))
        self.pushButton_sellall.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_sellall)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.groupBox)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_close = QPushButton(Widget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(100, 40))
        self.pushButton_close.setMaximumSize(QSize(100, 40))

        self.gridLayout_3.addWidget(self.pushButton_close, 0, 3, 1, 1)

        self.pushButton_stop = QPushButton(Widget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(100, 40))
        self.pushButton_stop.setMaximumSize(QSize(100, 40))

        self.gridLayout_3.addWidget(self.pushButton_stop, 0, 2, 1, 1)

        self.pushButton_start = QPushButton(Widget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(100, 40))
        self.pushButton_start.setMaximumSize(QSize(100, 40))

        self.gridLayout_3.addWidget(self.pushButton_start, 0, 1, 1, 1)

        self.pushButton_reflash = QPushButton(Widget)
        self.pushButton_reflash.setObjectName(u"pushButton_reflash")
        self.pushButton_reflash.setMinimumSize(QSize(100, 40))
        self.pushButton_reflash.setMaximumSize(QSize(100, 40))

        self.gridLayout_3.addWidget(self.pushButton_reflash, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 2, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        ___qtablewidgetitem = self.tableWidget_status.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget_status.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Ammount", None));
        ___qtablewidgetitem2 = self.tableWidget_status.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Current price", None));
        ___qtablewidgetitem3 = self.tableWidget_status.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Ratio", None));
        self.spinBox_time.setPrefix("")
        ___qtreewidgetitem = self.treeWidget_coins.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Widget", u"Selection", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Status", None))
        ___qtablewidgetitem4 = self.tableWidget_tot.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"Name", None));
        ___qtablewidgetitem5 = self.tableWidget_tot.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"avg buy price", None));
        ___qtablewidgetitem6 = self.tableWidget_tot.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget", u"balance", None));
        ___qtablewidgetitem7 = self.tableWidget_tot.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Widget", u"Current Price", None));
        ___qtablewidgetitem8 = self.tableWidget_tot.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Widget", u"Profit Ratio", None));
        self.groupBox.setTitle("")
        self.label_cname.setText(QCoreApplication.translate("Widget", u"Coin Name", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Price", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Price Ratio", None))
        self.label_amount.setText(QCoreApplication.translate("Widget", u"Amount", None))
        self.label_aratio.setText(QCoreApplication.translate("Widget", u"Amount Ratio", None))
        self.pushButton_sellcur.setText(QCoreApplication.translate("Widget", u"sell current ", None))
        self.pushButton_selllimit.setText(QCoreApplication.translate("Widget", u"sell  limit", None))
        self.pushButton_sellall.setText(QCoreApplication.translate("Widget", u"sell current All", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Total", None))
        self.pushButton_close.setText(QCoreApplication.translate("Widget", u"Close", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Widget", u"Stop", None))
        self.pushButton_start.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.pushButton_reflash.setText(QCoreApplication.translate("Widget", u"Reflash", None))
    # retranslateUi

