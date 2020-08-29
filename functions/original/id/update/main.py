import json
from google.cloud import datastore

client = datastore.Client('speech-similarity')


def original_voice_update(request):

    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'originalVoiceId' in request_json:
        user_id = request_json['originalVoiceId']
    elif request_args and 'originalVoiceId' in request_args:
        user_id = int(request_args['originalVoiceId'])
    else:
        # return error apiresponse
        return ""

    # check authentification and autorization

    with client.transaction():
        key = client.key('OriginalVoice', user_id)
        user = client.get(key)

        for arg, val in request_json.items():
            if arg != 'originalVoiceId':
                user[arg] = val
        client.put(user)

    return json.dumps({})
