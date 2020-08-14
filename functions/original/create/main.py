from google.cloud import datastore

datastore_client = datastore.Client('speech-similarity')


def original_voice_create(request):

    request_json = request.get_json(silent=True)

    with datastore_client.transaction():
        incomplete_key = datastore_client.key('OriginalVoice')
        user = datastore.Entity(key=incomplete_key)
        user.update(request_json)
        datastore_client.put(user)

    # firebase interaction for authentication
    # register and save in database/firestore user object
    return "User successfully registered"
