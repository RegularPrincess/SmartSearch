from business import Query


class MasterMiner:
    # формирование запроса Query
    def draw_schedule(self):
        """Здесь, например, ввод с клавиатуры..."""
        query = Query.create()
        print("Введите запрос по тегу:")
        input_text = input()
        if input_text == '':
            return None
        query.tag = input_text
        return query

    # обновить View
    def show_goods(self,data_chest):
        for good in data_chest:
            print(good)
        return None
