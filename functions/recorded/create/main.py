import json
import logging
import datetime
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
    bucket = storage_client.get_bucket(RESULT_BUCKET)
    blob = bucket.blob(filename+'.wav')
    blob.upload_from_file(wav_file)
    
    voice = {'filename': filename,
             'voiceUrl': 'https://storage.googleapis.com/{}/{}.wav'.format(RESULT_BUCKET, filename),
             'created': datetime.datetime.utcnow()}

    print(voice)

    # with datastore_client.transaction():
    #     incomplete_key = datastore_client.key('RecordedVoice')
    #     user = datastore.Entity(key=incomplete_key)
    #     user.update(voice)
    #     datastore_client.put(user)
    #
    # query = datastore_client.query(kind='RecordedVoice')
    # query.add_filter('voiceUrl', '=', voice['voiceUrl'])
    # results = list(query.fetch())
    # if len(results) > 0:
    #     voice['recordedVoiceId'] = results[0].key.id_or_name
    # else:
    #     return redirect(request.url)

    print(voice)
    # message = voice
    # message_data = json.dumps(message).encode('utf-8')
    # topic_path = publisher.topic_path(project_id, COMPARE_TOPIC)
    # future = publisher.publish(topic_path, data=message_data)
    # future.result()

    # firebase interaction for authentication
    # register and save in database/firestore user object
    return 'message_data'
