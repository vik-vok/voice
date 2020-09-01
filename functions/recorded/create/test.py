from google.cloud import datastore
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/nikalosa/Desktop/MACS/Final Project/MicroServices/Speech-Similarity-e6a5d5620dac.json"


datastore_client = datastore.Client('speech-similarity')

voice = {'filename':'bla', 'parentId':'123', 'userId':'123bla', 'voiceUrl':'hl.wav'}


with datastore_client.transaction():
    incomplete_key = datastore_client.key('RecordedVoice')
    user = datastore.Entity(key=incomplete_key)
    user.update(voice)
    datastore_client.put(user)
    print(user.key)

query = datastore_client.query(kind='RecordedVoice')
query.add_filter('voiceUrl', '=', voice['voiceUrl'])
results = list(query.fetch())

id = results[0].key.id_or_name
    # voice['recordedVoiceId'] = user.key
