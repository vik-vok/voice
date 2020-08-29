import json
from google.cloud import datastore

client = datastore.Client('speech-similarity')


def recorded_voice_get(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'recordedVoiceId' in request_json:
        voice_id = request_json['recordedVoiceId']
    elif request_args and 'recordedVoiceId' in request_args:
        voice_id = int(request_args['recordedVoiceId'])
    else:
        # return error apiresponse
        return ""

    key = client.key('RecordedVoice', voice_id)
    voice = client.get(key)

    return json.dumps(voice)
