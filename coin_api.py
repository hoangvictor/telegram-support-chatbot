from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def coin_price_response(coin):
    coin = coin.lower()

    try:
        tmp = cg.get_coin_market_chart_by_id(
            id=coin, vs_currency='usd', days=1)
        res = ('Actual price of {} : ${}\nActual market cap : ${}\nTotal volume today: ${}'.format(
            coin, tmp['prices'][-1][1], tmp['total_volumes'][-1][1], tmp['market_caps'][-1][1]))
    except:
        res = "No coin available, please check the coin name"

    return res
