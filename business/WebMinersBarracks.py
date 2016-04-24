# здесь покоится "бизнес-логика"
import requests
import json

# import time
# import calendar
#
# def epoch_time(string):
#     return calendar.timegm(time.strptime(string, "%d %m %Y"))

# from business import Query

# возвращает сырой json
# фильтрация происходила по:
# временному интервалу появления вопроса
# и рейтингу
def dig(schedule):
    request = requests.get("https://api.stackexchange.com/2.2/questions?page=1&pagesize=100&fromdate=1451606400&todate=1451692800&order=desc&min=1&max=100&sort=votes&site=stackoverflow")
    deserialized_request = json.loads(request.text)
    return deserialized_request

# возвращает список ссылок на вопросы
# фильтрация происходит по тегу из schedule
def craft(schedule, raw_data):
    output = []
    for data in raw_data["items"]:
        if schedule.tag in data["tags"]:
            output.append(data["link"])
    return output
