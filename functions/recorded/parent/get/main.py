import json
from google.cloud import datastore

client = datastore.Client('speech-similarity')


def recorded_voice_original_get(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'originalVoiceId' in request_json:
        parent_id = request_json['originalVoiceId']
    elif request_args and 'originalVoiceId' in request_args:
        parent_id = request_args['originalVoiceId']
    else:
        # error
        return "originalVoiceId Not Found in request"

    print(parent_id)
    query = client.query(kind='RecordedVoice')
    query.add_filter('originalVoiceId', '=',str(parent_id))
    # query.order = ['']
    results = list(query.fetch())
    print(results)
    query.keys_only()
    keys = list(query.fetch())

    for i in range(len(results)):
        results[i]['recordedVoiceId'] = keys[i].id

    return json.dumps(results)
