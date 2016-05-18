from MVC import queryProcessor


class ConsoleView:
    def __init__(self):
        pass

    def get_query(self):
        # можно вынести в константы
        # можно завести отдельную модель-диалог для помощника
        print('Available attributes: -tags, -sort, -max, -min')
        # print('How to use:\ntags=tag1;tag2;tag3\n-sort=vote/date\n[min,max] — range of question rate')
        print('Incorrect input == Crash of script')
        print('Try it:')

        raw_query = input()

        query = queryProcessor.format_query(raw_query)
        return queryProcessor.compile_request(query)

    def choose_question(self):
        number = int(input()) - 1
        return number
    # View "знает" реализацию question и answer
    # передавать сразу строки?
    # с другой стороны классы из stackoverflowsInstances нужны для того, чтобы не передавать строки
    def print_questions(self, questions):
        no = 1
        for question in questions:
            print(no, question.title)
            no += 1
        return None

    def print_answer(self, answer):
        print(answer.body)