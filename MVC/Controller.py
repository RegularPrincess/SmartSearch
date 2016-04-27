def mvc_run(model, view):
    query = view.get_query()
    data = model.handle_query(query)
    view.update(data)
    return None
