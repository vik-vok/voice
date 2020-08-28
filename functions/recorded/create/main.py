import json
import logging
from google.cloud import datastore
from google.cloud import storage
from google.cloud import pubsub_v1

project_id = 'speech-similarity'
RESULT_BUCKET = "recorded-voices"
COMPARE_TOPIC = "compare-topic"

storage_client = storage.Client()
publisher = pubsub_v1.PublisherClient()
datastore_client = datastore.Client(project_id)


def recorded_voice_create(request):
    # check if the post request has the file part
    request_json = request.get_json(silent=True)

    if 'audio_data' not in request.files:
        flash('No file part')
        return redirect(request.url)
        
    wav_file = request.files['audio_data']
    # if user does not select file, browser also
    # submit an empty part without filename
    if wav_file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    filename = wav_file.filename
    # print(request_json)
    bucket = storage_client.get_bucket(RESULT_BUCKET)
    blob = bucket.blob(filename)
    blob.upload_from_file(wav_file)

    voice = {'filename': filename, **request_json}
    voice['voiceUrl'] = 'https://storage.googleapis.com/{}/{}.wav'.format(RESULT_BUCKET, filename)

    print(filename)

    with datastore_client.transaction():
        incomplete_key = datastore_client.key('RecordedVoice')
        user = datastore.Entity(key=incomplete_key)
        user.update(voice)
        datastore_client.put(user)

    message = voice
    message_data = json.dumps(message).encode('utf-8')
    topic_path = publisher.topic_path(project_id, COMPARE_TOPIC)
    future = publisher.publish(topic_path, data=message_data)
    future.result()

    # firebase interaction for authentication
    # register and save in database/firestore user object
    return "Voice successfully registered"
