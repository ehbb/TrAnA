
import graphitesend

class Source:
    "Generic class that needs to be inherited by Source types (like Googlefinanace)"

    PROJECT = "trana"
    METRIC_PREFIX = PROJECT + ".digital.currency."
    METRIC_DELIM = "."
    METRIC_VALUE = "value"

    def run(self):
        ""

    def buildAndSendMetricToGraphite(self, trade_list):
        ""
        metric_list = []

        for data in trade_list:
            tsymbol = data.symbol
            tdate_time = data.date_time
            tvalue = data.value

            metric_name = self.build_metric(tsymbol)
            data = (metric_name, tvalue, tdate_time) # tuple
            metric_list.append(data)
            #self.send_to_graphite(metric_name, tdate_time, tvalue)

        self.send_to_graphite_as_list(metric_list)

    def build_metric(self, suffix):
        "Appends given suffix with the global value METRIC_PREFIX"
        # TODO: check whether METRIC_PREFIX ends with dot. Add it if it doesn't
        metric_name = (self.METRIC_PREFIX + suffix + self.METRIC_DELIM + self.METRIC_VALUE).lower()

        return metric_name

    def send_to_graphite(self, metric_name, date_time, value):
        "Sends metric to graphite"
        # TODO: Add logger
        print "metric_name: %s: %s (%s)" % (metric_name, value, date_time)
        # Build dict format to send metrics to graphite
        metrics_in_dict = {}

        # use grafitesend()

    def send_to_graphite_as_list(self, metric_list):
        "Sends metric to graphite"
        # TODO: Add logger
        #print "metric_name: %s: %s (%s)" % (metric_name, value, date_time)
        print "metric_list: %s" % metric_list

        # Build dict format to send metrics to graphite

        # use grafitesend()
        graphitesend.init(prefix = '', system_name = '', graphite_server = 'localhost', graphite_port = 2003)
        graphitesend.send_list(metric_list)
