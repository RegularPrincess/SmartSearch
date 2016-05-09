from business import StackoverflowsInstances
from business import StackoverflowAPI


# business-logic implementation
class StackoverflowCrawler:
    def __init__(self):
        pass

    def handle_query(self, query):
        # search for questions similar to query
        questions = StackoverflowAPI.API.search_questions(query)
        # get list of best answers
        top_answers = []
        for question in questions:
            answers = question.get_answers()
            if len(answers) > 0:
                top_answer = max(answers, key=lambda x: x.score)
                top_answers.append(top_answer)
        # return best of the best
        return max(top_answers, key=lambda x: x.score)
