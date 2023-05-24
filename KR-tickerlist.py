
import requests
import json
import pyupbit

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
print("====================================")
print(ret)
