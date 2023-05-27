import os
import jwt
import uuid
from urllib.parse import urlencode

import json
from common import *
from upbitApi import *
import ast
import pandas as pd
import requests

import numpy as np


class autoTradproc(QThread):
    poped = Signal(str)
    def __init__(self,coins,tm,ma_t1=20,ma_t2=60):
        super().__init__()
        self.working = True
        self.coinis= coins
        self.upbitapi= upbitApi()
        self.tm=tm
        self.ma_t1=ma_t1
        self.ma_t2=ma_t2

    def run(self):
        # 자동매매 시작
        while self.working:
            for coin in self.coins:
                data= self.uptbitapi.GetCandlesMinutes(coin,self.count,self.tm)
                df = pd.DataFrame(data)
                df=df['trade_price'].iloc[::-1]
                ma_1 = df.rolling(window=self.ma_t1, min_periods=1).mean()
                ma_2 = df.rolling(window=self.ma_t2, min_periods=1).mean()
                test1=ma_1.iloc[-2]-ma_1.iloc[-2]
                test2=ma_1.iloc[-1]-ma_1.iloc[-1]
                call='해당없음'
                if test1>0 and test2<0:
                    call='데드크로스'
                if test1<0 and test2>0:
                    call='골든크로스'
                logging.info(self.market)
                logging.info('이동평균선 20: ', round(ma_1.iloc[-1],2))
                logging.info('이동평균선 60: ', round(ma_2.iloc[-1],2))
                logging.info('골든크로스/데드크로스: ',call)
                logging.info('')
                time.sleep(1)
                try:
                    now = datetime.datetime.now()
                    start_time = self.upbitapi.get_start_time(coin)
                    end_time = start_time + datetime.timedelta(days=1)
                    if start_time < now < end_time - datetime.timedelta(seconds=10):
                        target_price = self.upbitapi.get_target_price(coin, 0.5)
                        ma20 = self.upbitapi.get_ma20(coin)
                        current_price = self.upbitapi.get_current_price(coin)

                    if target_price < current_price and ma20 < current_price:
                        bprice = self.upbitapi.get_balance(coin)
                        if bprice > 5000:
                            self.upbitapi.buy_market_order(coin, bprice*0.9995)
                    else:
                        sprice = self.upbitapi.get_balance(coin)
                        if sprice > 0.44:
                            self.upbitapi.sell_market_order(coin, sprice*0.9995)

                except Exception as e:
                    logging.info(e)
                    time.sleep(1)
   
    def stop(self):
        self.working = False
        self.quit()
        self.wait(5000) #5000ms = 5

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

class TradeStatus_proc(QThread):
    poped = Signal(str)

    def __init__(self,coin):
        super().__init__()
        self.working = True
        self.coin=coin
        self.upbitapi= upbitApi()
    
    def run(self):
        while (self.working):
            time.sleep(1)
            data=  self.upbitapi.GetTradesTicks(self.coin)
            param=('%s' %(data))
            self.poped.emit(param)
        

        
    def stop(self):
        self.working = False
        self.quit()
        self.wait(5000) #5000ms = 5    

class watch_proc(QThread):
    poped = Signal(str)

    def __init__(self):
        super().__init__()
        self.working = True
        
    
    def run(self):
        while (self.working):
            time.sleep(1)
            now = QtCore.QTime.currentTime()
            
            
            nowstr = now.toString('hh:mm:ss')
            param=('%s' %(nowstr))
            self.poped.emit(param)
        

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
        self.mon_TradeStatus=None
        self.watch_Timer =None
        self.tradesum_row =0
        self.upbit= upbitApi()
        self.coins=self.upbit.get_coins()
        self.balance=self.upbit.Getbalances()
        self.currentAll=self.upbit.GetCurrentAll()
        self.pjson_data = json.loads(json.dumps(self.currentAll))
        self.date = QDate.currentDate()
        logging.info("start upbit auto trade 1")
        self.ui.tableWidget_status.setStyleSheet(tblstyle)
        self.ui.tableWidget_tot.setStyleSheet(tblstyle)
        self.ui.tableWidget_tradesum.setStyleSheet(tblstyle)

        self.ui.tableWidget_status.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget_tot.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget_tradesum.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.pushButton_close.setStyleSheet(btnstylestr)
        self.ui.pushButton_start.setStyleSheet(btnstylestr)
        self.ui.pushButton_stop.setStyleSheet(btnstylestr)
        self.ui.pushButton_reflash.setStyleSheet(btnstylestr)
        self.ui.pushButton_sellcur.setStyleSheet(btnstylestr1)
        self.ui.pushButton_sellall.setStyleSheet(btnstylestr1)
        self.ui.pushButton_selllimit.setStyleSheet(btnstylestr1)

        self.ui.tableWidget_status.setColumnWidth(0, 160)
        self.ui.tableWidget_status.setColumnWidth(1, 100)
        self.ui.tableWidget_status.setColumnWidth(2, 100)
        self.ui.tableWidget_status.setColumnWidth(3, 50)
        self.ui.tableWidget_tot.setColumnWidth(0, 160)
        self.ui.tableWidget_tot.setColumnWidth(1, 60)
        self.ui.tableWidget_tot.setColumnWidth(2, 100)
        self.ui.tableWidget_tot.setColumnWidth(3, 70)
        self.ui.tableWidget_tot.setColumnWidth(4, 70)
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
        self.ui.show()
        self.set_updateAllData()
        self.start_watchTimer()

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
                
            
               
            if self.watch_Timer:
                self.watch_Timer.stop()                
                
            if self.mon_TradeStatus:
                self.mon_TradeStatus.stop()                
                                   
            QApplication.instance().quit()

        elif obj.objectName()=="pushButton_stop":
            if self.reflash_balance:
                self.reflash_balance.stop()
                
            if self.reflash_market:
                self.reflash_market.stop()
                
        elif obj.objectName()=="pushButton_start":
            logging.info('TBD')
            ret = self.upbit.GetOrderbook("KRW-BTC")
            logging.info(ret)

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
        self.ui.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
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

    def start_watchTimer(self):
        if self.watch_Timer:
            self.watch_Timer.stop()
        self.watch_Timer= watch_proc()
        self.watch_Timer.poped.connect(self.setwatch)
        self.watch_Timer.start()
        self.date = QDate.currentDate()
        self.ui.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.start_TradeStatus("KRW-BTC")
        
        
    def start_TradeStatus(self,coin):
        if self.mon_TradeStatus:
            self.mon_TradeStatus.stop()
        self.mon_TradeStatus= TradeStatus_proc(coin)
        self.mon_TradeStatus.poped.connect(self.setTradeStatus)
        self.mon_TradeStatus.start()
        
    @Slot('QString')
    def setTradeStatus(self,data):
        a=data.replace('[','')
        b=a.replace(']','')
           
        tmp=ast.literal_eval(str(b))
        jdata = json.loads(json.dumps(tmp))
        logging.info(jdata)
        '''
        'market': 'KRW-BTC', 
        'trade_date_utc': '2023-05-27', 
        'trade_time_utc': '14:08:48', 
        'timestamp': 1685196528667, 
        'trade_price': 35644000.0, 
        'trade_volume': 0.00015068, 
        'prev_closing_price': 35771000.0, 
        'change_price': -127000.0, 
        'ask_bid': 'BID', 
        'sequential_id': 1685196528667000}]
        '''
        self.tradesum_row = self.ui.tableWidget_tradesum.rowCount()
        self.ui.tableWidget_tradesum.insertRow(self.tradesum_row)
        tmp=jdata.get("trade_date_utc")
        logging.info(tmp)
        col0 =QTableWidgetItem(str(tmp))
        col0.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col0.setFlags(col0.flags()&~(Qt.ItemIsEditable))
        col0.setFlags(col0.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,0, col0)

        tmp=jdata.get("trade_time_utc")
        logging.info(tmp)
        col1 =QTableWidgetItem(str(tmp))
        col1.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col1.setFlags(col0.flags()&~(Qt.ItemIsEditable))
        col1.setFlags(col0.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,1, col1)

        tmp=jdata.get("timestamp")
        logging.info(tmp)
        col1 =QTableWidgetItem(str(tmp))
        col1.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col1.setFlags(col1.flags()&~(Qt.ItemIsEditable))
        col1.setFlags(col1.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,2, col1)
        
        tmp=jdata.get("trade_price")
        col2 =QTableWidgetItem(str(tmp))
        col2.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col2.setFlags(col2.flags()&~(Qt.ItemIsEditable))
        col2.setFlags(col2.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,3, col2)
        
        
        
        tmp=jdata.get("trade_volume")
        col4 =QTableWidgetItem(str(tmp))
        col4.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col4.setFlags(col4.flags()&~(Qt.ItemIsEditable))
        col4.setFlags(col4.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,4, col4)
        
        
        
        tmp=jdata.get("prev_closing_price")
        col5 =QTableWidgetItem(str(tmp))
        col5.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col5.setFlags(col5.flags()&~(Qt.ItemIsEditable))
        col5.setFlags(col5.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,5, col5)

        

        tmp=jdata.get("change_price")
        col6 =QTableWidgetItem(str(tmp))
        col6.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col6.setFlags(col6.flags()&~(Qt.ItemIsEditable))
        col6.setFlags(col6.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,6, col6)


        tmp=jdata.get("ask_bid")
        if tmp == 'ASK':
            col7 =QTableWidgetItem('매수')
        else:
            col7 =QTableWidgetItem('매도')
        
        col7.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col7.setFlags(col7.flags()&~(Qt.ItemIsEditable))
        col7.setFlags(col7.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,7, col7)

        tmp=jdata.get("sequential_id")
        col8 =QTableWidgetItem(str(tmp))
        col8.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        col8.setFlags(col8.flags()&~(Qt.ItemIsEditable))
        col8.setFlags(col8.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_tradesum.setItem(self.tradesum_row,8, col8)
        self.tradesum_row +=1

        
        
    @Slot('QString')
    def setwatch(self,data):
        
        self.date = QDate.currentDate()
        self.ui.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate) + " " + data) 
        #logging.info(self.coins)
    def set_updateAllData(self):
        QTimer.singleShot(500, self.set_tblBalance)
        QTimer.singleShot(500, self.set_tbleData)
        #QTimer.singleShot(3000, self.set_tbleReszie)

    def set_tbleReszie(self):
        self.ui.tableWidget_status.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_tradesum.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_tot.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.treeWidget_coins.header().setSectionResizeMode(0,QHeaderView.ResizeToContents)

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
        amtvol=""
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
            tmp = cdata.get('volume')
            amtvol=format(tmp,",")
            ratio = cdata.get('ratio')
        except Exception as e:
            logging.info('3. 예외가 발생했습니다. %s' %(cname))
            return


        pitem =QTableWidgetItem(str(cur))
        pitem.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        pitem.setFlags(pitem.flags()&~(Qt.ItemIsEditable))
        pitem.setFlags(pitem.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_status.setItem(row,2, pitem)

        vitem =QTableWidgetItem(str(f'{amtvol}백만'))
        vitem.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        vitem.setFlags(vitem.flags()&~(Qt.ItemIsEditable))
        vitem.setFlags(vitem.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_status.setItem(row,1, vitem)

        ritem =QTableWidgetItem(str(ratio))
        ritem.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        ritem.setFlags(ritem.flags()&~(Qt.ItemIsEditable))
        ritem.setFlags(ritem.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_status.setItem(row,3, ritem)

        strCname=json_data.get("korean_name")

        citem =QTableWidgetItem(f'{strCname} {cname}')
        citem.setFlags(citem.flags()&~(Qt.ItemIsEditable))
        citem.setFlags(citem.flags()|(Qt.ItemIsSelectable))
        self.ui.tableWidget_status.setItem(row,0, citem)
        self.setTreeView(self.ui.treeWidget_coins,f'{strCname} {cname}')
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

