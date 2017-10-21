from googlefinance import getQuotes
#import src.main.common.Source.Source

class GoogleFinance():

    def getData(self):
        quote = getQuotes('AAPL')
        print quote
        return None

obj = GoogleFinance()
obj.getData()