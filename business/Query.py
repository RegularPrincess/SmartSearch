def create():
    return Query()


class Query:
    pages = None
    page_size = None
    # question
    q_from_date = "2015 1 1"
    q_to_date = "2016 4 24"
    q_min_vote = 1
    q_max_vote = 100
    # answers
    a_from_date = None
    a_to_date = None
    a_min_vote = None
    a_max_vote = None
    # query
    tag = "c++"
