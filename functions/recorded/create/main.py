import json

from google.cloud import datastore
from google.cloud import storage
from google.cloud import pubsub_v1

project_id = 'speech-similarity'
RESULT_BUCKET = "recorded-voices"
COMPARE_TOPIC = "compare-topic"

storage_client = storage.Client()
# publisher = pubsub_v1.PublisherClient()
# datastore_client = datastore.Client(project_id)


def recorded_voice_create(request):

    request_json = request.get_json(silent=True)
    filename = request_json['name']
    # print(request_json)
    wav_file = request.files['audio_data']
    bucket = storage_client.get_bucket(RESULT_BUCKET)
    blob = bucket.blob()
    blob.upload_from_file(wav_file)

    request_json['voiceUrl'] = 'https://storage.googleapis.com/{}/{}.wav'.format(RESULT_BUCKET, filename)

    print(filename)

    # with datastore_client.transaction():
    #     incomplete_key = datastore_client.key('RecordedVoice')
    #     user = datastore.Entity(key=incomplete_key)
    #     user.update(request_json)
    #     datastore_client.put(user)

    # message = request_json
    # message_data = json.dumps(message).encode('utf-8')
    # topic_path = publisher.topic_path(project_id, COMPARE_TOPIC)
    # future = publisher.publish(topic_path, data=message_data)
    # future.result()

    # firebase interaction for authentication
    # register and save in database/firestore user object
    return "Voice successfully registered"
