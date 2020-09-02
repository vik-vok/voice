import json
from google.cloud import datastore

client = datastore.Client('speech-similarity')


def original_voice_get(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'originalVoiceId' in request_json:
        voice_id = request_json['originalVoiceId']
    elif request_args and 'originalVoiceId' in request_args:
        voice_id = int(request_args['originalVoiceId'])
    else:
        # return error apiresponse
        return ""

    key = client.key('OriginalVoice', voice_id)
    voice = client.get(key)
    
    with client.transaction():
        voice['views'] += 1
        voice.update(voice)
        client.put(voice)
    
    voice['originalVoiceId'] = voice_id
    return json.dumps(voice)