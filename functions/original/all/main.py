import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def original_voice_get_all(request):
    query = datastore_client.query(kind='OriginalVoice')
    results = list(query.fetch())

    return json.dumps(results)
