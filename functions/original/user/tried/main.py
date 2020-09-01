import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def original_voice_user_tried(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'userId' in request_json:
        userId = request_json['userId']
    elif request_args and 'userId' in request_args:
        userId = request_args['userId']
    else:
        return (
            json.dumps({"error": "Missing parameter: userId"}),
            422,
            {})

    # fetch data
    query = datastore_client.query(kind='OriginalVoice')
    query.add_filter('userId', '=', userId)
    results = list(query.fetch())

    # fetch keys for given data
    query.keys_only()
    keys = list(query.fetch())
    for i in range(len(results)):
        results[i]['originalVoiceId'] = keys[i].id

    results = sorted(results, key=lambda voice: -voice.get('views', 0))
    return json.dumps(results)