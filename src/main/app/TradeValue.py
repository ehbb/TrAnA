
class TradeValue:
    ""
    symbol = ""
    name = ""
    value = -1
    date_time = 0

    def __repr__(self):
        ret = "[symbol: %s , name: %s , value: %s , date_time: %s ]" % (self.symbol,
                                                                        self.name,
                                                                        self.value,
                                                                        self.date_time)
        return  ret



