import json
from google.cloud import datastore

client = datastore.Client('speech-similarity')


def recorded_voice_get(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'voiceId' in request_json:
        voice_id = request_json['voiceId']
    elif request_args and 'voiceId' in request_args:
        voice_id = int(request_args['voiceId'])
    else:
        # return error apiresponse
        return ""

    key = client.key('RecordedVoice', voice_id)
    voice = client.get(key)

    return json.dumps(voice)
