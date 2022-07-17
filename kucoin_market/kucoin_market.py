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
        self.__set_constants()

    def __set_constants(self):
        self._seperator = "-"
        self._marketName = "kucoin"
        self._webSocketBaseAddress = ""
        self._webSocketOrderBookAddress = ""

    def get_symbols_exchange_info(self):
        symbols = self.__client.get_symbols()
        return symbols

    @staticmethod
    def filter_exchange_info_with_usdt_quote_asset(all_coins_exchange_info):
        for index in range(len(all_coins_exchange_info) - 1, -1, -1):
            if all_coins_exchange_info[index]["quoteCurrency"] != "USDT":
                del all_coins_exchange_info[index]

    @staticmethod
    def get_base_coin_names(exchange_info):
        coin_names = []
        for info in exchange_info:
            coin_names.append(info["baseCurrency"])
        return coin_names






