import json


def original_voice_voices(request):
    result = [{
        "id": 132,
        "parentid": 14,
        "voiceUrl": "bla.blu",
        "userId": 12
    }]

    # convert into JSON:
    return json.dumps(result)
