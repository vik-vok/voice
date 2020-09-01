import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def recored_voice_user_original(request):
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

    if request_json and 'originalVoiceId' in request_json:
        originalVoiceId = request_json['originalVoiceId']
    elif request_args and 'originalVoiceId' in request_args:
        originalVoiceId = request_args['originalVoiceId']
    else:
        return (
            json.dumps({"error": "Missing parameter: originalVoiceId"}),
            422,
            {})

    # fetch data
    query = datastore_client.query(kind='RecordedVoice')
    query.add_filter('userId', '=', userId)
    query.add_filter('originalVoiceId', '=', originalVoiceId)
    results = list(query.fetch())

    # fetch keys for given data
    query.keys_only()
    keys = list(query.fetch())
    for i in range(len(results)):
        results[i]['recordedVoiceId'] = keys[i].id
    
    results = sorted(results, key=lambda voice: -voice.get('views', 0))
    return json.dumps(results)