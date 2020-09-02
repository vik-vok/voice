import json

from flask import flash, redirect
from google.cloud import datastore
from google.cloud import storage

storage_client = storage.Client()
datastore_client = datastore.Client("speech-similarity")
RESULT_BUCKET = "original-voices"
KIND = "OriginalVoice"


def original_voice_create(request):
    # 1. Validate that file exists
    if "audio_data" not in request.files:
        flash("No file part")
        return redirect(request.url)

    # 2. get audio file
    wav_file = request.files["audio_data"]
    if wav_file.filename == "":
        flash("No selected file")
        return redirect(request.url)
    filename = wav_file.filename

    # 3. Upload file in the bucket
    bucket = storage_client.get_bucket(RESULT_BUCKET)
    blob = bucket.blob(filename + ".wav")
    blob.upload_from_file(wav_file)
    path = "https://storage.googleapis.com/{}/{}.wav".format(RESULT_BUCKET, filename)

    # 4. Store data in the OriginalVoice Datastore
    voice = {
        "name": request.form.get("name"),
        "path": path,
        "userId": request.form.get("userId"),
        "avatar": request.form.get("avatar"),
        "views": 0,
    }

    # 5. Update View Count
    try:
        with datastore_client.transaction():
            incomplete_key = datastore_client.key(KIND)
            user = datastore.Entity(key=incomplete_key)
            user.update(voice)
            datastore_client.put(user)
    except:
        pass

    # 6. Query for ID
    query = datastore_client.query(kind=KIND)
    query.add_filter("path", "=", voice["path"])
    results = list(query.fetch())
    if len(results) > 0:
        voice["originalVoiceId"] = results[0].key.id_or_name
    else:
        return redirect(request.url)

    # 7. Dump and return JSON
    message = voice
    message_data = json.dumps(message).encode("utf-8")

    return message_data, 200, headers
