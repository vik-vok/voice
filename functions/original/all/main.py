import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def original_voice_get_all(request):
    # query = datastore_client.getAll(kind='OriginalVoice')
    # results = list(query.fetch())

    query = datastore_client.query(kind='OriginalVoice')
    query.keys_only()
    kinds = [entity.key for entity in query.fetch()]

    return json.dumps(kinds)
