from flask import current_app

def add_to_index(index, model):
    if not current_app.elastisearch:
        return

    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elastisearch.index(index=index, id=model.id, body=payload)

def remove_from_index(index, model):
    if not current_app.elastisearch:
        return

    current_app.elastisearch.delete(index=index, id=model,id)

def query_index(index, query, page, per_page):
    if not current_app.elastisearch:
        return [], 0

    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]

    return ids, search['hits']['total']['value']
