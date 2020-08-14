import json


def recorded_voice_get(request):
    result = {
        "title": "voice1",
        "description": "desc1",
    }

    # convert into JSON:
    # test comment
    return json.dumps(result)
