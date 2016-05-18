from API import stackoverflowAPI


class Owner:
    id = None
    nick = None

    def __init__(self, json_info):
        if 'user_id' in json_info:
            self.id = json_info['user_id']
        self.nick = json_info['display_name']


class Comment:
    def __init__(self, json_info):
        self.id = json_info['comment_id']
        self.owner = Owner(json_info['owner'])
        self.body = json_info['body_markdown']
        self.creation_date = json_info['creation_date']


class Answer:
    def __init__(self, json_info):
        self.id = json_info['answer_id']
        self.owner = Owner(json_info['owner'])
        self.body = json_info['body_markdown']
        self.creation_date = json_info['creation_date']
        self.score = json_info['score']
        self.__comments = None

    def get_comments(self):
        if self.__comments is None:
            self.__comments = stackoverflowAPI.get_answer_comments(self.id)

        return self.__comments


class Question:
    def __init__(self, json_info):
        self.id = json_info['question_id']
        self.owner = Owner(json_info['owner'])
        self.body = json_info['body_markdown']
        self.creation_date = json_info['creation_date']
        self.score = json_info['score']
        self.answer_count = json_info['answer_count']
        self.title = json_info['title']
        self.tags = json_info['tags']
        self.__answers = None
        self.__comments = None

    def get_comments(self):
        if self.__comments is None:
            self.__comments = stackoverflowAPI.get_question_comments(self.id)
        return self.__comments

    def get_answers(self):
        if self.__answers is None:
            self.__answers = stackoverflowAPI.get_answers(self.id)
        return self.__answers
