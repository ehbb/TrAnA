from googlefinance import getQuotes
from src.main.coinmarketcap.CoinMKCSource import CoinMKCSource
from src.main.common.Source import Source
import json

class Main:
    GOOGLE_FINANCE = 1
    COIN_MARKET_CAP = 2

    def main(self):
        # Read source file to know the source type
        source_type = self.getSourceType()
        source = Source()

        # get the appropriate object
        if source_type == self.GOOGLE_FINANCE:
            print "Souce is GOOGLE_FINANCE"
        elif source_type == self.COIN_MARKET_CAP:
            print "Source is COIN_MARKET_CAP"
            source = CoinMKCSource()

        source.run()


    def getSourceType(self):
        # type: () -> object
        # TODO: Implement this function.
        # Read from property file
        #ret = self.GOOGLE_FINANCE
        ret = self.COIN_MARKET_CAP
        return ret


#print json.dumps(getQuotes('AAPL'), indent=2)
obj = Main()
obj.main()

