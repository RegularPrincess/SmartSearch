import datetime
import time


ATTRIBUTE_MARK = '-'
ATTRIBUTE_SPLITTER = '='
DATE_SPLITTER = '.'
SPACE = ' '
NOTHING = ''


def _get_unixtime(date_string):
    """Дата в формате (год, месяц, день) -> (unix-секунды)"""
    splitted_date = date_string.split(DATE_SPLITTER)
    y = splitted_date[0]
    m = splitted_date[1]
    d = splitted_date[2]
    date = _create_date(y, m, d)
    return int(time.mktime(date.timetuple()))


def _create_date(y, m, d):
    """Новый объект типа date"""
    return datetime.date(y, m, d)


# empty dictionary
def create_empty_query():
    query = dict(intitle=None, fromdate=None, todate=None, tags=None, sort=None, min=None, max=None)
    return query


# raw_query -> structured_query
# string -> dictionary
def format_query(raw_query):
    structured_query = create_empty_query()
    attributes = raw_query.split(ATTRIBUTE_MARK)
    structured_query['intitle'] = attributes.pop(0)

    for attribute in attributes:
        splitted_attribute = attribute.split(ATTRIBUTE_SPLITTER)
        attribute_name = splitted_attribute[0]
        attribute_value = splitted_attribute[1]
        structured_query[attribute_name] = attribute_value

    # атрибуты даты пока не доступны
    # if structured_query['fromdate'] is not None:
    #     structured_query['fromdate'] = _get_unixtime(structured_query['fromdate'])
    # if structured_query['todate'] is not None:
    #     structured_query['todate'] = _get_unixtime(structured_query['todate'])

    return structured_query


def compile_request(structured_query):
    """Сборка HTTP запроса"""
    request = []

    if structured_query['intitle'] is not None:
        request.append("intitle=%s" % structured_query['intitle'])

    if structured_query['fromdate'] is not None:
        request.append("fromdate=%s" % structured_query['fromdate'])

    if structured_query['todate'] is not None:
        request.append("todate=%s" % structured_query['todate'])

    if structured_query['tags'] is not None:
        request.append("tagged=%s" % structured_query['tags'])

    # sort options
    if structured_query['sort'] is not None:
        request.append("sort=%s" % structured_query['sort'])

    if structured_query['min'] is not None:
        request.append("min=%s" % structured_query['min'])

    if structured_query['max'] is not None:
        request.append("max=%s" % structured_query['max'])

    return "&".join(request)
