# зачем плодить классы, если у python такая уютная система процедур и модулей?
import WebMinersBarracks


# handle_query : schedule, craft_scheme -> data_chest
def handle_query(schedule):
    # На основе интересующих пользователя свойств (дата, рейтинг и т.д.) из schedule,
    # получаем "сырой" json с вопросами со StackOverFlow.
    raw_data = WebMinersBarracks.dig(schedule)
    # Используем schedule и "сырой" json с вопросами,
    # чтобы найти интересующие пользователя ответы.
    data_chest = WebMinersBarracks.craft(schedule, raw_data)
    # возвращаем данные в формате, который можно скормить View
    return data_chest
