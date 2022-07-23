from kucoin.client import Client

from base_market.base_market import BaseMarket
from . import credentials


class KucoinMarket(BaseMarket):
    def __init__(self):
        BaseMarket.__init__(self)
        self.__apiKey = credentials.publicKey
        self.__apiSecret = credentials.secretKey
        self.__passphrase = credentials.passphrase
        self.__client = Client(api_key=self.__apiKey, api_secret=self.__apiSecret, passphrase=self.__passphrase)
        self._set_constants()

    def _set_constants(self):
        self._seperator = "-"
        self._marketName = "kucoin"
        self._quoteKeyName = "quoteCurrency"
        self._baseAssetKeyName = "baseCurrency"
        self._tetherName = "USDT"

    def get_symbols_exchange_info(self):
        symbols = self.__client.get_symbols()
        return symbols

    def get_last_500_1h_kline_data(self, coin_name):
        full_name = coin_name + self._seperator + self._tetherName
        start_time = int(self._get_time_500h_before_in_ms() / 1000)
        return self.__client.get_kline_data(symbol=full_name, kline_type="1hour", start=start_time)