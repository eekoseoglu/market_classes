from binance.client import Client
from binance.enums import KLINE_INTERVAL_1HOUR

from base_market.base_market import BaseMarket
from . import credentials


class BinanceMarket(BaseMarket):
    def __init__(self):
        BaseMarket.__init__(self)
        self.__apiKey = credentials.publicKey
        self.__apiSecret = credentials.secretKey
        self.__client = Client(api_key=self.__apiKey, api_secret=self.__apiSecret)
        self._set_constants()

    def _set_constants(self):
        self._seperator = "/"
        self._marketName = "binance"
        self._quoteKeyName = "quoteAsset"
        self._baseAssetKeyName = "baseAsset"
        self._tetherName = "USDT"

    def get_symbols_exchange_info(self):
        symbols = self.__client.get_exchange_info()["symbols"]
        return symbols

    def get_last_500_1h_kline_data(self, coin_name):
        full_name = coin_name + self._tetherName
        start_time = self._get_time_500h_before_in_ms()
        kliens = self.__client.get_historical_klines(symbol=full_name, interval=KLINE_INTERVAL_1HOUR, start_str= start_time)
        kliens.reverse()
        return kliens
