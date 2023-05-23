import os
import jwt
import uuid
from urllib.parse import urlencode

import json
from common import *
from upbitApi import *
import ast

class reflash_marketproc(QThread):
    poped = Signal(str)

    def __init__(self,coins):
        super().__init__()
        self.working = True
        self.coins= coins
        self.row =0

    def run(self):
        self.row=0
        for it in self.coins:
            time.sleep(0.001)
            if self.working==False:
               break
            param=('%s@%s' %(self.row,it))
            self.poped.emit(param)
            time.sleep(0.05)
            self.row +=1

        logging.info('done!')

    def stop(self):
        self.working = False
        self.quit()
        self.wait(5000) #5000ms = 5

class reflash_balanceproc(QThread):
    poped = Signal(str)

    def __init__(self,balance):
        super().__init__()
        self.working = True
        self.balance= balance
        self.row =0

    def run(self):
        self.row=0
        for it in self.balance:
            time.sleep(0.001)
            if self.working==False:
               break
            param=('%s@%s' %(self.row,it))
            self.poped.emit(param)
            self.row +=1

        logging.info('done!')

    def stop(self):
        self.working = False
        self.quit()
        self.wait(5000) #5000ms = 5


class LoginDlg(QDialog):
    """login dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file_name = LOGINUI_FILE
        ui_file = QFile(ui_file_name)
        self.config = configparser.ConfigParser()
        self.config.read(CFG_FILE, encoding='utf-8')
        self.access_key=self.config['KeyInfo']['access']
        self.security_key=self.config['KeyInfo']['security']
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
        self.ui.lineEdit_aes.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_sec.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_aes.setText(self.access_key)
        self.ui.lineEdit_sec.setText(self.security_key)
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
        self.ui.label_aes.setStyleSheet(labelstylestr)
        self.ui.label_sec.setStyleSheet(labelstylestr)
        self.ui.lineEdit_aes.setStyleSheet(lineedstylestr)
        self.ui.lineEdit_sec.setStyleSheet(lineedstylestr)

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
        self.reflash_market= None
        self.reflash_balance= None
        self.upbit= upbitApi()
        self.coins=self.upbit.get_coins()
        self.balance=self.upbit.Getbalances()
        self.currentAll=self.upbit.GetCurrentAll()
        self.pjson_data = json.loads(json.dumps(self.currentAll))
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
#        self.set_tblBalance()
#        self.set_tbleData()
        self.set_btnevt()
        self.ui.tableWidget_status.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_tot.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.show()
        self.set_updateAllData()

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
            if self.reflash_balance:
                self.reflash_balance.stop()

            if self.reflash_market:
                self.reflash_market.stop()
            QApplication.instance().quit()

        elif obj.objectName()=="pushButton_stop":
            if self.reflash_balance:
                self.reflash_balance.stop()
            if self.reflash_market:
                self.reflash_market.stop()
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

    def closeEvent(self,event):
        logging.info("Main close")
        if self.reflash_balance:
            self.reflash_balance.stop()

        if self.reflash_market:
            self.reflash_market.stop()

    def set_btnevt(self):
        self.ui.pushButton_start.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_start))
        self.ui.pushButton_stop.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_stop))
        self.ui.pushButton_close.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_close))
        self.ui.pushButton_reflash.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_reflash))
        self.ui.pushButton_sellcur.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_reflash))
        self.ui.pushButton_selllimit.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_reflash))
        self.ui.pushButton_sellall.clicked.connect(lambda x:self.btn_event(self.ui.pushButton_reflash))
        self.ui.closeEvent = self.closeEvent


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

    @Slot('QString')
    def setbalance(self,data):
        tmp=data.split("@")
        row = int(tmp[0])
        it=ast.literal_eval(tmp[1])
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
            try:
                ratio=round((float(cur)/float(avg) *100.0)-100.0,2)
            except Exception as e:
                logging.info('예외가 발생했습니다. %s' %(cname))
                ratio=0
                pass
            col4 =QTableWidgetItem(str(ratio))
            col4.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            if ratio == 0:
                col4.setForeground(Qt.black)
            elif ratio < 0:
                col4.setForeground(Qt.blue)
            else:
                col4.setForeground(Qt.red)
            self.ui.tableWidget_tot.setItem(row,4, col4)

    def set_tblBalance(self):
        self.ui.tableWidget_tot.setRowCount(0)
        balance = self.upbit.Getbalances()
        if self.reflash_balance:
            self.reflash_balance.stop()
        self.reflash_balance= reflash_balanceproc(balance)
        self.reflash_balance.poped.connect(self.setbalance)
        self.reflash_balance.start()


        #logging.info(self.coins)
    def set_updateAllData(self):
        QTimer.singleShot(500, self.set_tblBalance)
        QTimer.singleShot(500, self.set_tbleData)

    def set_tbleData(self):
        self.ui.tableWidget_status.setRowCount(len(self.coins))
        if self.reflash_market:
            self.reflash_market.stop()
        self.reflash_market= reflash_marketproc(self.coins)
        self.reflash_market.poped.connect(self.setcoinsinfo)
        self.reflash_market.start()


    @Slot('QString')
    def setcoinsinfo(self,data):
        cname=""
        cur=0
        vol=""
        it=data.split("@")
        row = int(it[0])
        coin = it[1]
        coin=ast.literal_eval(it[1])
        json_data = json.loads(json.dumps(coin))
        cname=json_data.get("market")
        cur=self.pjson_data.get(cname)

        try:
            tmp=self.upbit.GetCurrentInfo(1,cname)
            cinfo=ast.literal_eval(tmp)
            cdata = json.loads(json.dumps(cinfo))
            vol = cdata.get('volume')
            ratio = cdata.get('ratio')
        except Exception as e:
            logging.info('3. 예외가 발생했습니다. %s' %(cname))
            return


        pitem =QTableWidgetItem(str(cur))
        pitem.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        if ratio == 0:
            pitem.setForeground(Qt.black)
        elif ratio < 0:
            pitem.setForeground(Qt.blue)
        else:
            pitem.setForeground(Qt.red)
        self.ui.tableWidget_status.setItem(row,2, pitem)

        vitem =QTableWidgetItem(str(vol))
        vitem.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.ui.tableWidget_status.setItem(row,1, vitem)

        ritem =QTableWidgetItem(str(ratio))
        ritem.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.ui.tableWidget_status.setItem(row,3, ritem)

        strCname=json_data.get("korean_name")

        citem =QTableWidgetItem(strCname)
        self.ui.tableWidget_status.setItem(row,0, citem)
        self.setTreeView(self.ui.treeWidget_coins,strCname)
        if ratio == 0:
            pitem.setForeground(Qt.black)
            ritem.setForeground(Qt.black)
            citem.setForeground(Qt.black)
            vitem.setForeground(Qt.black)
        elif ratio < 0:
            pitem.setForeground(Qt.blue)
            ritem.setForeground(Qt.blue)
            vitem.setForeground(Qt.blue)
            citem.setForeground(Qt.blue)
        else:
            pitem.setForeground(Qt.red)
            ritem.setForeground(Qt.red)
            vitem.setForeground(Qt.red)
            citem.setForeground(Qt.red)


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

