class Model:
    # BusinessModel business_model

    def __init__(self, business_model):
        self.business_model = business_model

    # query -> list<string>
    def handle_query(self, query):
        # паровозик.который.смог(чух-чух)
        return self.business_model.work(query)
