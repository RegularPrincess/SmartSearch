from API import stackoverflowAPI


# Model
# business-logic implementation
class StackoverflowCrawler:
    def __init__(self):
        self._questions = None

    def search_questions(self, query):
        # search for questions similar to query
        questions = stackoverflowAPI.search_questions(query)
        self._questions = questions
        return questions

    def question_by_number(self, number):
        question = self._questions[number]
        return question

    def best_answer(self, question):
        answers = question.get_answers()
        top_answer = max(answers, key=lambda x: x.score)
        return top_answer
