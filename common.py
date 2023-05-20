import os
from PySide2 import QtCore, QtGui
import platform 
from multiprocessing import Process, freeze_support
import sys,traceback
from PySide2.QtUiTools import QUiLoader
import logging
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel
from PySide2 import QtWidgets
from PySide2.QtCore import Qt,QFile, QIODevice,QStringListModel \
,QDateTime,QTimer,QThread ,QProcess,Signal,Slot
from PySide2.QtWidgets import *
import json
import configparser
import argparse
import netifaces as ni
import subprocess
from decimal import Decimal
from enum import Enum
import time
logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
     datefmt='%Y-%m-%d:%H:%M:%S', level=logging.INFO)

tblstyle='''
 QHeaderView::section {
          spacing: 10px;
          background-color:darkblue;
          color: white;
          margin: 1px;
          text-align: right;
          font-family: Arial;
          font-size:10px; }
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
 

UI_FILE = "main.ui"
LOGINUI_FILE = "login.ui"
