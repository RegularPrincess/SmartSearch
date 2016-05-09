class View:
    def __init__(self, view_impl):
        self.view_impl = view_impl

    def get_query(self):
        return self.view_impl.get_query()

    # обновить View на основе информации из data
    def update(self, data):
        self.view_impl.update(data)
        return None
