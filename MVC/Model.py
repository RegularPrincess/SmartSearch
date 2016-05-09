class Model:

    def __init__(self, business_model):
        self.business_model = business_model

    def handle_query(self, query):
        return self.business_model.handle_query(query)
