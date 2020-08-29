import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def recorded_voice_get_all(request):
    query = datastore_client.query(kind='RecordedVoice')
    results = list(query.fetch())

    query.keys_only()
    keys = list(query.fetch())

    for i in range(len(results)):
        results[i]['recordedVoiceId'] = keys[i].id

    return json.dumps(results)
