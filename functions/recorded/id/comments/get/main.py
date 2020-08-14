import json


def recorded_voice_comments(request):
    result = [{
        "id": 123,
        "comment": "avoie",
        "voiceid": 14,
        "userId": 12
    }]

    # convert into JSON:
    # test
    return json.dumps(result)
