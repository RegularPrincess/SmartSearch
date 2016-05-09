import datetime
import time
from business import StackoverflowAPI


def get_unixtime(date):
    return int(time.mktime(date.timetuple()))


def compile_request(intitle=None, fromdate=None, todate=None, tags=None):
    parameters = []

    if intitle is not None:
        parameters.append("intitle=%s" % intitle)

    if fromdate is not None:
        parameters.append("fromdate=%s" % get_unixtime(fromdate))

    if todate is not None:
        parameters.append("todate=%s" % get_unixtime(todate))

    if tags is not None:
        parameters.append("tagged=%s" % ";".join(tags))

    return "&".join(parameters)


# параметры запроса, задаются извне. Если параметр не задан, то должен быть None
fromdate = datetime.date(2016, 1, 1)
todate = datetime.date.today()
tags = ['c++', 'iterator']
intitle = 'string'

# ответы, отсортированные по релевантности
questions = StackoverflowAPI.API.search_questions(compile_request(intitle, fromdate, todate, tags))

# изначально ответы на вопрос не загружены. при первом вызове функции идёт запрос на сайт, дальнейшие вызовы просто возвращают значение
answers = questions[0].get_answers()

# так же с комментами у ответов и вопросов
comments_answer = answers[1].get_comments()
comments_question = questions[0].get_comments()

print(5)
