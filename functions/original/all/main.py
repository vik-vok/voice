import json


def voice_handler(request):
    voice1 = {
        "title": "voice1",
        "description": "desc1",
    }
    voice2 = {
        "title": "voice2",
        "description": "desc2",
    }
    voice3 = {
        "title": "voice3",
        "description": "desc3",
    }
    voice4 = {
        "title": "voice4",
        "description": "desc4",
    }

    result = [voice1, voice2, voice3, voice4]

    # convert into JSON:
    return json.dumps(result)
