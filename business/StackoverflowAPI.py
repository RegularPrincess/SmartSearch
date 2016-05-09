import json
import requests
from business import StackoverflowsInstances

# HTTP requests consts:
HTTP_SEARCH_QUESTIONS = "http://api.stackexchange.com/2.2/search?site=stackoverflow&filter=!*Jxe6D.tT)zEcHZX&%s"
HTTP_GET_ANSWERS = "http://api.stackexchange.com/2.2/questions/%s/answers?order=desc&sort=activity&site=stackoverflow&filter=!1zSsisQasSFwU(q(36FWv"
HTTP_GET_QUESTIONS_COMMENTS = "http://api.stackexchange.com/2.2/questions/%s/comments?order=desc&sort=creation&site=stackoverflow&&filter=!1zSsisQasVU2CYS0yMFLZ"
HTTP_GET_ANSWERS_COMMENTS = "http://api.stackexchange.com/2.2/answers/%s/comments?order=desc&sort=creation&site=stackoverflow&filter=!1zSsisQasWN8(Zz1-z7RB"


class API:
    @staticmethod
    def get_question_comments(question_id):
        comments = []
        comments_json = json.loads(requests.get(HTTP_GET_QUESTIONS_COMMENTS % question_id).content.decode())['items']

        for comment_json in comments_json:
            comments.append(StackoverflowsInstances.Comment(comment_json))

        return comments

    @staticmethod
    def get_answer_comments(answer_id):
        comments = []
        comments_json = json.loads(requests.get(HTTP_GET_ANSWERS_COMMENTS % answer_id).content.decode())['items']

        for comment_json in comments_json:
            comments.append(StackoverflowsInstances.Comment(comment_json))

        return comments

    @staticmethod
    def search_questions(joined_parameters):
        questions = []
        url = HTTP_SEARCH_QUESTIONS % joined_parameters
        questions_json = json.loads(requests.get(url).content.decode())['items']

        for question_json in questions_json:
            questions.append(StackoverflowsInstances.Question(question_json))

        return questions

    @staticmethod
    def get_answers(question_id):
        answers = []
        answers_json = json.loads(requests.get(HTTP_GET_ANSWERS % question_id).content.decode())['items']

        for answer_json in answers_json:
            answers.append(StackoverflowsInstances.Answer(answer_json))

        return answers
