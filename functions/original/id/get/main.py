import json


def original_voice_handler(request):
    result = {
        "title": "voice1",
        "description": "desc1",
    }

    # convert into JSON:
    return json.dumps(result)
