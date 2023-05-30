
import requests
import json
import pyupbit
access = 'AVkrSuvV2ZvfQLDc67jWxlHRTHAD5zWDRH7JsIAC'
security = 'FmYDmMJxIukg7m1Hm0PIZNWd5mM8GILleB2WhxWx'

# 원화 시장 티커목록 조회
market = "KRW-BTC"
#krw_tickers = pyupbit.get_tickers("KRW")
#print("== 원화(KR) 시장의 종목을 조회합니다 ==")
#print("")
#print("종목 리스트 : ", krw_tickers)
#print("종목 개수 : ", len(krw_tickers))

url = "https://api.upbit.com/v1/trades/ticks"

querystring = {"market": "KRW-BTC", "count": "1"}

response = requests.request("GET", url, params=querystring)

ret = json.loads(response.text)
print("++++++++++++++++++++++++++++++++++++++++++++")
print(ret)
url = "https://api.upbit.com/v1/orderbook"

querystring = {"markets": market}

response = requests.request("GET", url, params=querystring)

ret = json.loads(response.text)
#print("====================================")
#print(ret)

df = pyupbit.get_ohlcv(ticker="KRW-BTC",interval='day',count=20)
#print(df)
ma20 = df['close'].rolling(window=20, min_periods=1).mean().iloc[-1]
#print(ma20)


#df = pyupbit.get_ohlcv(ticker="KRW-BTC",interval='minute1',count=12)
#print(df)
upbit = pyupbit.Upbit(access, security)
res =  upbit.get_balances()
print (res)
