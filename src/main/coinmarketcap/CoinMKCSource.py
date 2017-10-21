from src.main.common.Source import Source
import urllib, json
from src.main.app.TradeValue import TradeValue


# import requests
#########################
# Pulls data from CoinMarketCap.
#########################
class CoinMKCSource(Source):
    ""
    att_t_id = ""
    att_t_name = ""
    att_t_sybmol = ""
    att_t_value_in_usd = ""
    att_t_last_updatetime = ""

    def __init__(self):
        self.att_t_id = "id"
        self.att_t_name = "name"
        self.att_t_sybmol = "symbol"
        self.att_t_value_in_usd = "price_usd"
        self.att_t_last_updatetime = "last_updated"

    # TODO: Read this value from config file.
    URL = "https://api.coinmarketcap.com/v1/ticker/"

    def run(self):
        "Starts the process of Analyzing Digital currencies from CoinMarketCap"
        # Get the result from API
        response = urllib.urlopen(self.URL)
        data = response.read()
        jsonData = json.loads(data)
        # print data

        trade_list = self.getDataInStandardForm(jsonData)
        #t = trade_list.pop()
        print trade_list

        # Create metric and send it to Graphite
        self.buildAndSendMetricToGraphite(trade_list)
        # Get the backup

        #

    def getDataInStandardForm(self, raw_data):
        "Returns a list of Trade values in the standard format i.e. class TradeValue"
        if type(raw_data) is not list:
            print "Expected input is list. EXITING"
            exit(1)

        trade_list = list()
        for data in raw_data:
            trade = TradeValue()

            trade.symbol = data[self.att_t_sybmol]
            trade.name = data[self.att_t_name]
            trade.value = data[self.att_t_value_in_usd]
            trade.date_time = data[self.att_t_last_updatetime]
            #print trade.symbol + ", "
            trade_list.append(trade)

        return trade_list
