import pyupbit
import hashlib
import requests
import os
import uuid
import jwt
import json
import ast
from urllib.parse import unquote, quote, quote_plus, urlencode

from common import *
#기본 변수 설정
server_url = "https://api.upbit.com"

class upbitApi:
    def __init__(self):

        self.config = configparser.ConfigParser()
        self.config.read(CFG_FILE, encoding='utf-8')
        self.access_key=self.config['KeyInfo']['access']
        self.secret_key=self.config['KeyInfo']['security']
        self._favlist=ast.literal_eval(self.config['favlist']['markets'])
        self._autoact=ast.literal_eval(self.config['autoact']['markets'])
        self._autolist=ast.literal_eval(self.config['autolist']['markets'])
        self.server_url= server_url
        self.payload = {
        'access_key': self.access_key,
        'nonce': str(uuid.uuid4()),
    }

        self.coins=self.get_coins()
        self.jwt_token = jwt.encode(self.payload, self.secret_key)
        self.authorize_token = 'Bearer {}'.format(self.jwt_token)
        self.headers = {"Authorization": self.authorize_token}
        self.upbit_connect()

    @property
    def favlist(self):

        return self._favlist

    @favlist.setter
    def favlist(self,value):

        self.adddel_favlist(value)
        self.config['favlist']['markets']=str(self._favlist)
        with open(CFG_FILE, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    @property
    def autoact(self):

        return self._autoact

    @autoact.setter
    def autoact(self,value):

        self.adddel_autoact(value)
        self.config['autoact']['markets']=self._autoact
        with open(CFG_FILE, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def adddel_autoact(self,val):
        for it in self._autoact:
            if it == val:
                self._autoact.remove(val)
                return  self._autoact
        return self._autoact

    @property
    def autolist(self):
        return self._autolist


    @autolist.setter
    def autolist(self,val):
        self.adddel_autolist(val)
        self.config['autolist']['markets']=str(self._autolist)
        with open(CFG_FILE, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def adddel_autolist(self,val):
        for it in self._autolist:
            if it == val:
                self._autolist.remove(val)
                return  self._autolist

        self._autolist.append(val)


    def adddel_favlist(self,fav):
        for it in self._favlist:
            if it == fav:
                self._favlist.remove(fav)
                return  self._favlist

        self._favlist.append(fav)
        return self._favlist

    def adddel_favlist(self,val):
        for it in self._autoact:
            if it == val:
                return  self._autoact

        self._autoact.append(val)
        return self._autoact

    def del_autoact(self,val):
        for it in self._autoact:
            if it == val:
                self._autoact.remove(val)
        return self._autoact


    def del_favlist(self,fav):
        for it in self._favlist:
            if it == fav:
                self._favlist.remove(fav)
        return self._favlist

    def get_autolist(self):
        return self._autolist

    def set_autolist(self,autolist):
        self._autolist=autolist

    def upbit_connect(self):
        upbit = pyupbit.Upbit(self.access_key, self.secret_key)
        res =  upbit.get_balances()
        self.balance=res
        return res
    # 한글이름
    def get_coins(self):
        coins = pyupbit.get_tickers(fiat='KRW', verbose=True,is_details=False)
        return coins


    # 주문 - 주문 가능 정보
    def GetOrdersChance(self, market):
        query = {
            'market': market,
        }
        query_string = urlencode(query).encode()

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        self.payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
         'query_hash_alg': 'SHA512',
         }


        res = requests.get(self.server_url + "/v1/orders/chance",
                        params=query, headers=self.headers)

        ret = res.json()

        return ret

   # 주문 - 개별 주문 조회
    def GetOrder(self):
        query = {
            'uuid': '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',
        }
        query_string = urlencode(query).encode()

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        res = requests.get(self.server_url + "/v1/order", params=query, headers=self.headers)

        ret = res.json()

        return ret

        # 주문 - 주문 리스트 조회
    def GetOrders(self):
        res = requests.get(self.server_url + "/v1/orders", headers=self.headers)
        ret = res.json()
        return ret

    # 주문 - 주문하기(Buy) : 지정가
    def PostOrders_Buy(self, market, volume, price):
        query = {
            'market': market,
            'side': 'bid',
            'volume': volume,
            'price': price,
            'ord_type': 'limit',
        }
        query_string = urlencode(query).encode()

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()

        res = requests.post(self.server_url + "/v1/orders", params=query, headers=self.headers)
        ret = res.json()
        return ret

    # 주문 - 주문하기(Buy) : 시장가
    def PostOrders_Buy_Auto(self, market, price):
        query = {
        'market': market,
        'side': 'bid',
        'price': price,
        'ord_type': 'price',
        }
        query_string = urlencode(query).encode()

        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()
        res = requests.post(self.server_url + "/v1/orders", params=query, headers=self.headers)
        ret = res.json()
        return ret
    # 이동 평균 값
    def GetMA(self,inter, cnt,coin="KRW-BTC"):
        df = pyupbit.get_ohlcv(ticker=coin, interval=inter, count=cnt)
        ma = df['close'].rolling(window=cnt, min_periods=1).mean().iloc[-1]

    def get_current_price(self,ticker):
        """현재가 조회"""
        return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

    def get_ma20(self,ticker):
        """20일 이동 평균선 조회"""
        df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
        ma20 = df['close'].rolling(window=20, min_periods=1).mean().iloc[-1]

        return ma20

    def get_target_price(self,ticker, k):
        """변동성 돌파 전략으로 매수 목표가 조회"""
        df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
        k = 1 - abs(df.iloc[0]['open'] - df.iloc[0]['close']) / (df.iloc[0]['high'] - df.iloc[0]['low'])
        target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
        logging.info(target_price)
        return target_price

    def get_start_time(self,ticker):
        """시작 시간 조회"""
        df = pyupbit.get_ohlcv(ticker, interval="minute1", count=1)
        start_time = df.index[0]
        return start_time

    def sell_market_order(self,coin,price):
        pyupbit.sell_market_order(coin, price)

    def buy_market_order(self,coin,price):
        pyupbit.buy_market_order(coin, price)


    def GetCurrentInfo(self,min, coin="KRW-BTC"):
        i =0
        vol=""
        ratio=0
        mprice=0
        dprice=0
        mintval= f'minute{min}'
        while(i<3):
            try:
                dinfo = pyupbit.get_ohlcv(ticker=coin, interval='day', count=2, to=None, period=0)
                vol = dinfo['value'].values[1]
                dprice = dinfo['close'].values[0]
                minfo = pyupbit.get_ohlcv(ticker=coin, interval=mintval, count=1, to=None, period=0)
                mprice= minfo['close'].values[0]
                break
            except Exception as e:
                if i ==2:
                    logging.info(f'예외가 발생했습니다. {coin} {e}')
                time.sleep(0.1)
                i +=1
                continue
        try:
            ratio=round((float(mprice)/float(dprice) *100.0)-100.0,2)
        except Exception as e:
            logging.info('예외가 발생했습니다. %s' %(cname))
            ratio=0
            pass
        avol= round(vol/1000000)
#        logging.info(f'makrket: [{coin}] Now: [{mprice}]  Before: [{dprice}]  Ratio:[{ratio}] amount: [{avol}]')
        info='{"volume": %s,"ratio":%s}'  %(avol,ratio)
        return info

    def min_candle(self,min, coin="KRW-BTC"):
        # 1분봉 (최대 200개 요청가능)
        minute = pyupbit.get_ohlcv(coin, min)
        logging.info(minute)
        logging.info(type(minute), minute.shape)

    # 현재
    def GetCurrent(self,coin=["KRW-BTC"]):
        cur=pyupbit.get_current_price(coin)

        return cur

    def GetCurrentAll(self):
        clist=[]
        for it in self.coins:
            json_data = json.loads(json.dumps(it))
            cname=json_data.get("market")
            clist.append(cname)
        cur=self.GetCurrent(clist)

        return cur


    def Getbalances(self):
        return self.balance


    # 시세 캔들 조회 - 월(Months) 캔들
    def GetCandlesWeeks(self, market, count):
        url = "https://api.upbit.com/v1/candles/months"

        querystring = {"market": market, "count": count}

        response = requests.request("GET", url, params=querystring)

        ret = json.loads(response.text)

        return ret

    # 시세 캔들 조회 - min 캔들
    def GetCandlesMinutes(self, market, count,tm):

        url = f'https://api.upbit.com/v1/candles/minutes/{tm}'
        querystring = {"market":market,"count":str(count)}
        response = requests.request("GET", url, params=querystring)
        ret = json.loads(response.text)
        return ret


    # 시세 체결 조회 - 최근 체결 내역
    def GetTradesTicks(self,coin):
        url = "https://api.upbit.com/v1/trades/ticks"

        querystring = {"market": coin, "count": "1"}

        response = requests.request("GET", url, params=querystring)

        ret = json.loads(response.text)

        return ret

    # 시세 Ticker 조회 - 현재가 정보
    def GetTicker(self, market):
        url = "https://api.upbit.com/v1/ticker"

        querystring = {"markets": market}

        response = requests.request("GET", url, params=querystring)

        ret = json.loads(response.text)

        return ret

    # 시세 호가 정보(Orderbook) 조회
    def GetOrderbook(self, market):
        url = "https://api.upbit.com/v1/orderbook"

        querystring = {"markets": market}

        response = requests.request("GET", url, params=querystring)

        ret = json.loads(response.text)

        return ret
