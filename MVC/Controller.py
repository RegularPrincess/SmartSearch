def mvc_run(model, view):
    # запрос к сайту и получение списка похожих вопросов
    query = view.get_query()
    questions = model.search_questions(query)
    view.print_questions(questions)
    # выбор из списка вопросов
    question = model.question_by_number(view.choose_question())
    # получение ответа
    view.print_answer(model.best_answer(question))
    return None
