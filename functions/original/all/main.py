import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def original_voice_get_all(request):
    query = datastore_client.query(kind='OriginalVoice')
    results = list(query.fetch())

    query.keys_only()
    keys = list(query.fetch())

    for i in range(len(results)):
        entity = results[i]
        entity['id'] = keys[i].id.id_or_name
    return json.dumps(results)
