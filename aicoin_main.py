import os
import jwt
import uuid
from urllib.parse import urlencode

import json
from common import *
from upbitApi import *


def main():
     logging.info("start upbit auto trade")
     if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
         QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
     if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
         QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
     app = QApplication(sys.argv)
     logging.info(QStyleFactory.keys())
     if 'qtct-styel' in QStyleFactory.keys():
         app.setStyle("qt5ct-style");
     else:
         app.setStyle("Fusion");
     app.setWindowIcon(QtGui.QIcon('./appico.svg'))
     ex = MainWindow()
     sys.exit(app.exec_())

class LoginDlg(QDialog):
    """login dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file_name = LOGINUI_FILE
        ui_file = QFile(ui_file_name)
        
        if not ui_file.open(QIODevice.ReadOnly):
            logging.error("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)
        ui_file.close()
        loader = QUiLoader()
        window = loader.load(ui_file)
        if not window:
            logging.error(loader.errorString())
            sys.exit(-1)
        
        self.ui=window
        self.connected = False
        self.ui.show()
        
    def closeEvent(self,event):    
        logging.info("close")
        self.connected = False
        
    def confirmed(self):    
        return self.connected
            
        
            
    def btn_event(self,obj):                                                    

        if obj.objectName()=="pushButton_ok":                                   
            self.ui.close()                                                          
            self.connected = True
        else:
            self.connected = False
            QApplication.instance().quit() 
            sys.exit(-1)

                                                                                 
            
    def setStyle(self):     
        self.ui.pushButton_exit.setStyleSheet(btnstylestr)                                                   
        self.ui.pushButton_ok.setStyleSheet(btnstylestr)                                                   
        self.ui.pushButton_ok.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_ok))
        self.ui.pushButton_exit.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_exit))
        self.ui.closeEvent = self.closeEvent                                    
            
    def showDlg(self):                                                        
        self.setStyle()
        self.ui.show()                                                          
        return self.ui.exec_()    

class MainWindow(QMainWindow):

    def main__init__(self):
        logging.info("start upbit auto trade ")
        self.itemChanged=False
        self.coinitems=[]
        self.upbit= upbitApi()
        self.coins=self.upbit.get_coins()
        self.balance=self.upbit.Getbalances()
        self.currentAll=self.upbit.GetCurrentAll()
        logging.info("start upbit auto trade 1")
        self.ui.tableWidget_status.setStyleSheet(tblstyle)
        self.ui.tableWidget_tot.setStyleSheet(tblstyle)
        self.ui.pushButton_close.setStyleSheet(btnstylestr)
        self.ui.pushButton_start.setStyleSheet(btnstylestr)
        self.ui.pushButton_stop.setStyleSheet(btnstylestr)
        self.ui.pushButton_reflash.setStyleSheet(btnstylestr)
        self.ui.pushButton_sellcur.setStyleSheet(btnstylestr)
        self.ui.pushButton_sellall.setStyleSheet(btnstylestr)
        self.ui.pushButton_selllimit.setStyleSheet(btnstylestr)

        self.ui.tableWidget_status.setColumnWidth(0, 180)
        self.ui.tableWidget_status.setColumnWidth(1, 280)
        self.ui.tableWidget_status.setColumnWidth(2, 180)
        self.ui.tableWidget_status.setColumnWidth(3, 100)
        self.ui.treeWidget_coins.header().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.ui.treeWidget_coins.itemClicked.connect(lambda x:
                self.onItemClicked(self.ui.treeWidget_coins,
                self.ui.treeWidget_coins.currentItem(),
               self.ui.treeWidget_coins.currentColumn(),
               self.ui.tableWidget_status))
        logging.info("start upbit auto trade 2")
        self.ui.tabWidget.setCurrentIndex(0)
        self.set_tbleData()
        self.set_tblBalance()
        self.set_btnevt()
        self.ui.tableWidget_status.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_tot.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.show()

    def findTableItmes(self,key,tblwidget):
        fitems = tblwidget.findItems(key,Qt.MatchExactly)
        if not fitems:
            return
        for item in fitems:
            tblwidget.selectRow(item.row())

    def onItemClicked(self, tree,it, col,tblwidget):
        if col == -1:
            return
        #logging.info("col %d ",col)
        txt=str(it.text(col))
        logging.info("onItemClicked")
        txt=str(it.text(col))
        pitem=it.parent()
        logging.info("col %d, txt %s ",col,txt)
        if pitem:
            txt=str(pitem.text(0))
        else:
            logging.info("select parent item")
        x=txt.split("]", 1)
        sel=x[0].replace("[","")
        if self.itemChanged==True:
            logging.info("show all items")
            self.show_selectedItmes(tblwidget,tree)
            self.show_selectedItmes(self.ui.tableWidget_Framelog,tree)
        else:
            logging.info("show one item")
            self.findTableItmes(sel,tblwidget)
        self.itemChanged=False



    def tblselectRow(self,tbl,row):
         logging.info(row)
         logging.info(tbl.objectName())
         if tbl.objectName()=='tableWidget_coins':
             frame=tbl.item(row,2).text()
             desttbl=self.ui.tableWidget_status
             fitems = desttbl.findItems(frame,Qt.MatchExactly)
             for it in fitems:
                 desttbl.selectRow(it.row())
                 break

    def setcmbData(self):
        ratiolist=[10,20]
        self.ui.comboBox_pratio.add(ratiolist)

    def settblEvent(self):
        self.ui.tableWidget_coins.clicked.connect(lambda x: self.tblselectRow( self.ui.tableWidget_coins, self.ui.tableWidget_coins.currentRow()))



    def btn_event(self,obj):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        if obj.objectName()=="pushButton_close":
             QApplication.instance().quit()
        elif obj.objectName()=="pushButton_stop":
            logging.info('TBD')
        elif obj.objectName()=="pushButton_start":
            logging.info('TBD')
        elif obj.objectName()=="pushButton_reflash":
            self.set_tbleData()
            self.set_tblBalance()
        elif obj.objectName()=="pushButton_selcur":
            logging.info('TBD')
        elif obj.objectName()=="pushButton_selalll":
            logging.info('TBD')
        elif obj.objectName()=="pushButton_sellimit":
            logging.info('TBD')
        else:
            logging.info('no action')
        QApplication.restoreOverrideCursor()

    def set_btnevt(self):
        self.ui.pushButton_start.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_start))
        self.ui.pushButton_stop.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_stop))
        self.ui.pushButton_close.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_close))
        self.ui.pushButton_reflash.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_reflash))
        self.ui.pushButton_sellcur.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_reflash))
        self.ui.pushButton_selllimit.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_reflash))
        self.ui.pushButton_sellall.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_reflash))


    def setTreeView(self,tree,it):
        itemTop1 = QTreeWidgetItem(tree)
        itemTop1.setForeground(0, Qt.darkGreen)
        itemTop1.setText(0,it)
        itemTop1.setFlags(itemTop1.flags() | Qt.ItemIsUserCheckable)
        itemTop1.setForeground(0,Qt.darkRed)
        itemTop1.setCheckState(0, Qt.Unchecked)

    def get_CoinName(self, coin):
        strCname=""
        for it in self.coins:
            json_data = json.loads(json.dumps(it))
            cname=json_data.get("market")
            if cname.find(coin) !=-1:
                strCname = json_data.get("korean_name")
                break
        return strCname

    def auto_trade(self,coins,inteval=60):
        ratio = 0
        sellprice =0
        if ratio <= -2:
            logging.info("sell all")
        elif ratio >= 2 :
            logging.info("check proce for sell for 5 min")
            sellprice == 1000


    def set_tblBalance(self):

        self.ui.tableWidget_tot.setRowCount(0)
        balance = self.upbit.Getbalances()
        for it in balance:
            cname = it.get("currency")
            avg= it.get("avg_buy_price")
            bal= it.get("balance")
            if cname != "KRW" and avg !="0":
                name=self.get_CoinName(cname)
                row = self.ui.tableWidget_tot.rowCount()
                self.ui.tableWidget_tot.insertRow(row)
                col0 =QTableWidgetItem(name)
                col0.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
                self.ui.tableWidget_tot.setItem(row,0, col0)
                col1 =QTableWidgetItem(avg)
                col1.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)
                self.ui.tableWidget_tot.setItem(row,1, col1)
                col2 =QTableWidgetItem(bal)
                col2.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
                self.ui.tableWidget_tot.setItem(row,2, col2)
                curname="KRW-"+cname
                cur=self.upbit.GetCurrent(curname)
                col3 =QTableWidgetItem(str(cur))
                col3.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
                self.ui.tableWidget_tot.setItem(row,3, col3)
                ratio=round((float(cur)/float(avg) *100.0)-100.0,2)
                col4 =QTableWidgetItem(str(ratio))
                col4.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
                if ratio == 0:
                    col4.setForeground(Qt.black)
                elif ratio < 0:
                    col4.setForeground(Qt.blue)
                else:
                    col4.setForeground(Qt.red)
                self.ui.tableWidget_tot.setItem(row,4, col4)


        #logging.info(self.coins)

    def set_tbleData(self):
        self.ui.tableWidget_status.setRowCount(len(self.coins))
        self.currentAll=self.upbit.GetCurrentAll()
        pjson_data = json.loads(json.dumps(self.currentAll))
        row = 0
        curinfo=""


        for it in self.coins:

            json_data = json.loads(json.dumps(it))
            cname=json_data.get("market")


            cur=0
            try:
               #cur=self.upbit.GetCurrent(cname)
               cur=pjson_data.get(cname)
            except Exception as e:
               logging.info('예외가 발생했습니다. %s' %(cname))
               pass
            i =0
            vol=""
            while(i<2):
               try:
                    curinfo=self.upbit.GetCurrentInfo(cname)
                    logging.info(curinfo)
                    vol = curinfo['volume'].values[0]
                    break
               except Exception as e:
                    logging.info('예외가 발생했습니다. %s' %(cname))
                    time.sleep(0.01)
                    i +=1
                    continue


            pitem =QTableWidgetItem(str(cur))
            pitem.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.ui.tableWidget_status.setItem(row,2, pitem)

            vitem =QTableWidgetItem(str(vol))
            vitem.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.ui.tableWidget_status.setItem(row,1, vitem)


            strCname=json_data.get("korean_name")

            citem =QTableWidgetItem(strCname)
            self.ui.tableWidget_status.setItem(row,0, citem)
            self.setTreeView(self.ui.treeWidget_coins,strCname)


            row +=1

    def __init__(self):
        super(MainWindow, self).__init__()
        
        
        
        ui_file_name = UI_FILE
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            logging.error("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)
        ui_file.close()
        loader = QUiLoader()
        window = loader.load(ui_file)
        if not window:
            logging.error(loader.errorString())
            sys.exit(-1)
        self.ui=window
        self.logindlg = LoginDlg(self.ui)
        self.logindlg.showDlg()
        while (self.logindlg.confirmed() ==False):
            logging.info("wait loging")
            QApplication.instance().quit() 
            sys.exit(-1)
        self.evtype=1
        self.ui.installEventFilter(self)
        self.ui.eventFilter = self.eventFilter
        self.main__init__()
        
        
        1


if __name__ == "__main__":
    freeze_support()
    try:
        parser = argparse.ArgumentParser(description='--dbg <0,1,2,3> ')
        parser.add_argument('--dbg', required=False)
        args = parser.parse_args()
        if args.dbg=='0':
            logger.setLevel(logging.ERROR)
        elif args.dbg=='1':
            logger.setLevel(logging.WARNING)
        elif args.dbg=='2':
            logger.setLevel(logging.DEBUG)
        elif args.dbg=='3':
            logger.setLevel(logging.INFO)
        else:
            logger.setLevel(logging.ERROR)
    except:
        logger.setLevel(logging.ERROR)
        pass


    main()

