class Query:
    # question
    # интервал по дате:
    from_date = "2015 1 1"
    to_date = "2016 4 24"
    # answers
    a_min_vote = 1
    # список тегов
    tags = []
    # текст запроса
    query = ""

    def html_string(self):
        # Собрать данные из полей в html запрос, который можно скормить API сайта
        return None
