from binance_market.binance_market import BinanceMarket
from kucoin_market.kucoin_market import KucoinMarket

binance = BinanceMarket()
exchange_info_binance = binance.get_symbols_exchange_info()
binance.filter_exchange_info_with_usdt_quote_asset(exchange_info_binance)
crypto_names_binance = binance.get_base_coin_names(exchange_info_binance)
assert isinstance(crypto_names_binance, list)
for name in crypto_names_binance:
    print(name)
print("----------------------------------")
kucoin = KucoinMarket()
exchange_info_kucoin = kucoin.get_symbols_exchange_info()
kucoin.filter_exchange_info_with_usdt_quote_asset(exchange_info_kucoin)
crypto_names_kucoin = kucoin.get_base_coin_names(exchange_info_kucoin)
assert isinstance(crypto_names_kucoin, list)
for name in crypto_names_kucoin:
    print(name)
print("----------------------------------")
similarCoins = list(set(crypto_names_binance).intersection(crypto_names_kucoin))

for name in similarCoins:
    print(name)

print("----------------------------------")
