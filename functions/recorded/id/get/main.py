import json


def recorded_voice_get(request):
    result = {
        "title": "voice1",
        "description": "desc1",
    }

    # convert into JSON:
    return json.dumps(result)
