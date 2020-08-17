from google.cloud import datastore
from google.cloud import storage

storage_client = storage.Client()
datastore_client = datastore.Client('speech-similarity')
RESULT_BUCKET = "original-voices"


def original_voice_create(request):

    # error handling is missing

    request_json = request.get_json(silent=True)
    filename = request_json['name']
    wav_file = request.files['audio_data']
    bucket = storage_client.get_bucket(RESULT_BUCKET)
    blob = bucket.blob()
    blob.upload_from_file(wav_file)

    request_json['voiceUrl'] = 'https://storage.googleapis.com/{}/{}.wav'.format(RESULT_BUCKET, filename)

    with datastore_client.transaction():
        incomplete_key = datastore_client.key('OriginalVoice')
        user = datastore.Entity(key=incomplete_key)
        user.update(request_json)
        datastore_client.put(user)

    return "Voice successfully created"

