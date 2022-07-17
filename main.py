from binance_market.binance_market import BinanceMarket

binance = BinanceMarket()

exchange_info = binance.get_symbols_exchange_info()
binance.filter_exchange_info_with_usdt_quote_asset(exchange_info)
crypto_names = binance.get_base_coin_names(exchange_info)

assert isinstance(crypto_names, list)

for name in crypto_names:
    print(name)

