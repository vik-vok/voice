import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def recorded_voice_get_all(request):
    query = datastore_client.query(kind='RecordedVoice')
    return json.dump(list(query.fetch()))
