import MasterMiner


# get_query : принимает void -> возвращает query
# query (запрос) — реализован как запись
# её поля идентичны аргументам функции /questions из API сайта StackOverFlow
# смотри (https://api.stackexchange.com/docs/questions)
def get_query():
    return MasterMiner.draw_schedule()


# обновить View на основе информации из data_chest
def update(data_chest):
    MasterMiner.show_goods(data_chest)
    return None

