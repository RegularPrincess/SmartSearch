from business import Query


# формирование запроса Query
def draw_schedule():
    """Здесь, например, ввод с клавиатуры..."""
    query = Query.create()
    print("Введите запрос по тегу:")
    input_text = input()
    if input_text == '':
        return None
    query.tag = input_text
    return query


def show_goods(data_chest):
    if data_chest is None:
        print("Конец.")
        return None
    for good in data_chest:
        print(good)
    return None
