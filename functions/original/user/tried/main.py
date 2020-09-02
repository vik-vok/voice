import json
from google.cloud import datastore
from pprint import pprint as print

datastore_client = datastore.Client("speech-similarity")


def original_voice_user_tried(request):
    # 1. Check if userId field exists
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and "userId" in request_json:
        userId = request_json["userId"]
    elif request_args and "userId" in request_args:
        userId = request_args["userId"]
    else:
        return (json.dumps({"error": "Missing parameter: userId"}), 422, {})

    # 2. Fetch Data
    # 2.1 Fetch unique original voices keys for recorded voices
    query = datastore_client.query(kind="RecordedVoice")
    query.add_filter("userId", "=", userId)
    results = list(query.fetch())
    raw_keys = list(set([x["originalVoiceId"] for x in results]))

    # 2.2 Fetch unique original voices
    results = []
    keys = [datastore_client.key("OriginalVoice", int(x)) for x in raw_keys]
    for key in keys:
        originalVoice = datastore_client.get(key)
        originalVoice['originalVoiceId'] = key.id
        results.append(originalVoice)

    # 3. return unique original voices that was recorded by given user
    return json.dumps(results, indent=4, sort_keys=True, default=str)
