import time
from pprint import pprint


# import os, sys
# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(root + '/python')

# import logging
# logging.basicConfig(level = logging.DEBUG)


def diversify():
    # collect all balances across exchanges into wallets
    # then diversify into specific amounts
    # ex: 50% btc, 5% each of 8 next-top coins, 10x 1% of micro-caps
    for exchange in list_of_exchanges:
        print("\nExchange Balances: ")
        pprint(exchange.fetch_balance())
        time.sleep(3)
        # print(exchanges.fetch_deposit_address('USD'))
        # pprint(bitflyer.load_markets())
