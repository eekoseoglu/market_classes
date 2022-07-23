from abc import ABC, abstractmethod
import time

class BaseMarket(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _set_constants(self):
        pass

    @abstractmethod
    def get_symbols_exchange_info(self):
        pass

    @abstractmethod
    def get_last_500_1h_kline_data(self, coin_name):
        pass

    def filter_exchange_info_with_usdt_quote_asset(self, all_coins_exchange_info):
        for index in range(len(all_coins_exchange_info) - 1, -1, -1):
            if all_coins_exchange_info[index][self._quoteKeyName] != self._tetherName:
                del all_coins_exchange_info[index]

    def get_base_coin_names(self, exchange_info):
        coin_names = []
        for info in exchange_info:
            coin_names.append(info[self._baseAssetKeyName])
        return coin_names

    @staticmethod
    def _get_time_500h_before_in_ms():
        current_time_in_milliseconds = int(round(time.time() * 1000))
        start_time = current_time_in_milliseconds - 1800000000
        return start_time
