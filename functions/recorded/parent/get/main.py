import json
from google.cloud import datastore

client = datastore.Client('speech-similarity')


def recorded_voice_original_get(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'parentId' in request_json:
        parent_id = int(request_json['parentId'])
    elif request_args and 'parentId' in request_args:
        parent_id = int(request_args['parentId'])
    else:
        # error
        return "parentId Not Found in request"

    query = client.query(kind='RecordedVoice')
    query.add_filter('parentId', '=', parent_id)
    # query.order = ['']
    results = list(query.fetch())
    print(results)
    query.keys_only()
    keys = list(query.fetch())

    for i in range(len(results)):
        results[i]['id'] = keys[i].id

    return json.dumps(results)
