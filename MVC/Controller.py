from MVC import Model
from MVC import View


def mvc_run():
    """Берём в руки топор и организуем основной цикл программы."""
    AXE_IN_MY_HANDS = True
    # программа работает, пока пользователь продолжает посылать запросы
    # если запрос пустой, то это конец
    while AXE_IN_MY_HANDS:
        _mvc_step()
    return None


def _mvc_step():
    """
    Один "шаг" работы системы:
    1. получить запрос из View
    2. отправить его на обработку в Model
    3. обновить View, основываясь на полученных из Model данных
    """
    query = View.get_query()
    data = Model.handle_query(query)
    View.update(data)
    return None
