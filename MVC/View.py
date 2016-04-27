class View:
    def __init__(self, view_impl):
        self.view_impl = view_impl

    def get_query(self):
        return self.view_impl.draw_schedule()

    # обновить View на основе информации из data_chest
    def update(self, data_chest):
        self.view_impl.show_goods(data_chest)
        return None
