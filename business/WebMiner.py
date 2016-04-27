import requests
import json


# бизнес-логика:
class WebMiner:
    # string -> json
    def _dig(self, html):
        # Запрос к сайту с атрибутами: дата, рейтинг, тег.
        request = requests.get(html)
        # Возвращает список вопросов по тегу.
        json_request = json.loads(request.text)
        return json_request

    # json -> list<string>
    def _craft(self, query, json_raw_data):
        # Фильтруем. В списке вопросов ищем вопрос(-ы), похожий на вопрос(ы) пользователя.
        questions = self._sieve(json_raw_data)
        # Возвращаем ответы, по рейтингу не меньше указанного в запросе.
        answers = self._process(questions, query.a_max_vote)
        return answers

    # Работать! Солнце ещё высоко! (Или нет, мы же в шахте.)
    # Query -> list<string>
    def work(self, query):
        raw_json = self._dig(query.html_string())
        return self._craft(query, raw_json)
