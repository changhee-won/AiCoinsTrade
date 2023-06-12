import os
from PySide6 import QtCore, QtGui
import platform
from multiprocessing import Process, freeze_support
import sys,traceback
from PySide6.QtUiTools import QUiLoader
import logging
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel
from PySide6 import QtWidgets
from PySide6.QtCore import Qt,QFile, QIODevice,QStringListModel \
,QDateTime,QTimer,QThread ,QProcess,Signal,Slot,QDate
from PySide6.QtGui import QScreen
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import *
import json
import configparser
import argparse
import netifaces as ni
import subprocess
from decimal import Decimal
from enum import Enum
import time
from datetime import datetime
import configparser
from babel.numbers import format_decimal


CFG_FILE ="login.cfg"
logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
     datefmt='%Y-%m-%d:%H:%M:%S', level=logging.INFO)
#os.environ['UPBIT_OPEN_API_ACCESS_KEY'] = 'AVkrSuvV2ZvfQLDc67jWxlHRTHAD5zWDRH7JsIAC'
#os.environ['UPBIT_OPEN_API_SECRET_KEY'] = 'FmYDmMJxIukg7m1Hm0PIZNWd5mM8GILleB2WhxWx'
#access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
#secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
os.environ["PYSIDE_DESIGNER_PLUGINS"]="."
tblstyle_M = """
    QHeaderView::section {
          spacing: 10px;
          background-color:darkblue;
          color: yellow;
          margin: 1px;
          text-align: right;
          font-family: Arial;
          font-size:8px; }
    QTableWidget {
        background-color: black; 
        border-radius: 10px
    }

    QTableWidget::item {
        color: white;                    
        background-color: black;
        margin-top: 5px;          
        border-radius: 9px;
        padding-left: 5px;
    }

    QTableWidget::item:selected {
        background-color: yellow;
        color: blue;
    }
"""
tblstyle='''
 QHeaderView::section {
          spacing: 10px;
          background-color:darkblue;
          color: white;
          margin: 1px;
          text-align: right;
          font-family: Arial;
          font-size:8px; }
             QTableWidget {
        background-color: black; 
        border-radius: 10px
    }

    QTableWidget::item {
        color: white;                    
        background-color: black;
        margin-top: 5px;          
        border-radius: 9px;
        padding-left: 5px;
    }

    QTableWidget::item:selected {
        background-color: yellow;
        color: blue;
    }
 '''
tblstyle_A='''
 QHeaderView::section {
          spacing: 10px;
          background-color:darkred;
          color: white;
          margin: 1px;
          text-align: right;
          font-family: Arial;
          font-size:8px; }
          

  
 '''

cmbstyle='''
ComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
}
QComboBox {font: 8pt Arial;combobox-popup: 0;}
'''

btnstylestr = '''
 QPushButton{
        font: 8pt Arial Black;
        border-width: 2px;
        border-radius: 5px;
        font-weight: bold;
        border-color: beige;
        color: darkBlue;
        background-color: darkGray; }
 QPushButton:pressed {
     border-style: inset;
     background-color: red;
     }
 QPushButton:checked {color: white; background-color: red;}
 '''
btnstylestr1 = '''
 QPushButton{
        font: 8pt Arial Black;
        border-width: 3px;
        border-radius: 8px;
        font-weight: bold;
        border-color: beige;
        color: yellow;
        background-color: darkgreen; }
 QPushButton:pressed {
     border-style: inset;
     background-color: red;
     }
 QPushButton:checked {color: white; background-color: red;}
 '''
lineedstylestr = '''
 QLineEdit{
        font: 8pt Arial Black;
        border-width: 2px;
        border-radius: 5px;
        font-weight: bold;
        border-color: beige;
        color: darkBlue;}

  '''

labelstylestr = '''
 QLabel{
       font: 8pt Arial Black;
       font-weight: bold;
       color: darkRed;

         }
  '''


UI_FILE = "main1.ui"
LOGINUI_FILE = "login.ui"
