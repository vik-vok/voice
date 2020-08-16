import json
from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def original_voice_get_all(request):
    query = datastore_client.query(kind='OriginalVoice')
    headers = {
        'Content-type' : 'application/json',
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Headers' : 'Content-Type',
    }
    return json.dumps(list(query.fetch())), 200, headers
