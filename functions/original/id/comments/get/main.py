import json
import requests

COMMENTS_URL = 'https://vikvok-anldg2io3q-ew.a.run.app/comments/original/{}'
USERS_URL = 'https://vikvok-anldg2io3q-ew.a.run.app/users/{}'


def original_voice_comments(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'originalVoiceId' in request_json:
        voice_id = request_json['originalVoiceId']
    elif request_args and 'originalVoiceId' in request_args:
        voice_id = request_args['originalVoiceId']
    else:
        # return error apiresponse
        return ""

    comments_json = requests.get(COMMENTS_URL.format(voice_id)).json()
    for i, comment in enumerate(comments_json):
        user_id = comment['userID']
        user = requests.get(USERS_URL.format(user_id)).json()
        del comments_json[i]['userID']
        comments_json[i]['user'] = user

    return json.dumps(comments_json)
