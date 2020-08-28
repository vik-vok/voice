import json
import requests

RECORDED_VOICES_URL = 'https://vikvok-anldg2io3q-ew.a.run.app/recordedvoices/original/{}'
USERS_URL = 'https://vikvok-anldg2io3q-ew.a.run.app/users/{}'


def original_voice_recorded_voices(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'voiceId' in request_json:
        voice_id = request_json['voiceId']
    elif request_args and 'voiceId' in request_args:
        voice_id = request_args['voiceId']
    else:
        # error
        return ""

    voices_json = requests.get(RECORDED_VOICES_URL.format(voice_id)).json()
    for i, voice in enumerate(voices_json):
        user_id = voice['userId']
        user = requests.get(USERS_URL.format(user_id)).json()
        del voices_json[i]['userId']
        voices_json[i]['user'] = user

    return json.dumps(voices_json)

