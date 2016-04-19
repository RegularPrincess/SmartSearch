def create():
    return Query()


class Query:
    pages = "0"
    page_size = "100"
    # question
    q_from_date = "2007-01-01"
    q_to_date = "2007-12-31"
    q_min_vote = "0"
    q_max_vote = "0"
    # answers
    a_from_date = "2007-01-01"
    a_to_date = "2007-12-31"
    a_min_vote = "0"
    a_max_vote = "0"
    # query
    tags = "c++"
