import datetime
import time


class StumpView:
    def __init__(self):
        pass

    def _get_unixtime(self, date):
        return int(time.mktime(date.timetuple()))

    def _compile_request(self, intitle=None, fromdate=None, todate=None, tags=None):
        parameters = []

        if intitle is not None:
            parameters.append("intitle=%s" % intitle)

        if fromdate is not None:
            parameters.append("fromdate=%s" % self._get_unixtime(fromdate))

        if todate is not None:
            parameters.append("todate=%s" % self._get_unixtime(todate))

        if tags is not None:
            parameters.append("tagged=%s" % ";".join(tags))

        return "&".join(parameters)

    def get_query(self):
        intitle = 'bubblesort'
        fromdate = None
        todate = None
        tags = ['python', 'sort']

        return self._compile_request(intitle, fromdate, todate, tags)

    def update(self, data):
        print(data.body)
