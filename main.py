from binance_market.binance_market import BinanceMarket
from kucoin_market.kucoin_market import KucoinMarket

binance = BinanceMarket()
exchange_info_binance = binance.get_symbols_exchange_info()
binance.filter_exchange_info_with_usdt_quote_asset(exchange_info_binance)
crypto_names_binance = binance.get_base_coin_names(exchange_info_binance)
assert isinstance(crypto_names_binance, list)
kline_binance = binance.get_last_500_1h_kline_data("BTC")
print(type(kline_binance))
print(len(kline_binance))
print(kline_binance[0])
print("----------------------------------")


kucoin = KucoinMarket()
exchange_info_kucoin = kucoin.get_symbols_exchange_info()
kucoin.filter_exchange_info_with_usdt_quote_asset(exchange_info_kucoin)
crypto_names_kucoin = kucoin.get_base_coin_names(exchange_info_kucoin)
assert isinstance(crypto_names_kucoin, list)
# for name in crypto_names_kucoin:
#     print(name)
kline_kucoin = kucoin.get_last_500_1h_kline_data("BTC")
print(type(kline_kucoin))
print(len(kline_kucoin))
print(kline_kucoin[0])

print("----------------------------------")
similarCoins = list(set(crypto_names_binance).intersection(crypto_names_kucoin))

for name in similarCoins:
    print(name)

print("----------------------------------")
