import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def original_voice_get_all(request):
    query = datastore_client.query(kind='OriginalVoice')
    results = list(query.fetch())

    query.keys_only()
    keys = list(query.fetch())

    for i in range(len(results)):
        results[i]['originalVoiceId'] = keys[i].id

    results = sorted(results, key=lambda voice: -voice.get('views', 0))
    return json.dumps(results)
