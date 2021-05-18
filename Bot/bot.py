import tweepy


def authenticate(api_key, api_key_secret, access_tocken, access_tocken_secret):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_tocken, access_tocken_secret)
    return tweepy.API(auth)


def get_thread_text(api, author_id, status_id):
    thread = ''
    found = 0
    for status in tweepy.Cursor(api.user_timeline, id=author_id, tweet_mode='extended').items(500):
        if status.in_reply_to_user_id != author_id and status.in_reply_to_status_id is not None:
            continue
        elif status_id == status.id:
            found = 1
            thread = status.full_text + '\n' + thread
            if status.in_reply_to_status_id is None:
                break
        elif not status.in_reply_to_status_id is None:
            if status.in_reply_to_user_id == author_id:
                thread = status.full_text + '\n' + thread
            else:
                thread = ''
        elif found == 1:
            thread = status.full_text + '\n' + thread
            break
        else:
            thread = ''
    return thread


def get_mentioned_thread(api, last_seen_id_thread):
    mentions = api.mentions_timeline(last_seen_id_thread, tweet_mode='extended')
    if not mentions:
        return 0, 0, 0, 0
    mention = mentions[-1]
    last_seen_id_thread = mention.id
    status_id_thread = mention.in_reply_to_status_id
    author_id_thread = mention.in_reply_to_user_id
    user_id_thread = api.get_user(mention.id)
    return last_seen_id_thread, status_id_thread, author_id_thread, user_id_thread


def get_last_seen_id():
    return


def set_last_seen_id(last_seen_id):
    return


def update_db(thread_text, user):
    return


auth_api = authenticate()
while True:
    last_seen_id = get_last_seen_id()
    last_seen_id, status_id, author_id, user = get_mentioned_thread(auth_api, last_seen_id)
    if last_seen_id == 0 and status_id == 0 and author_id == 0 and user == 0:
        continue
    set_last_seen_id(last_seen_id)
    thread = get_thread_text(auth_api, author_id, status_id)
    update_db(thread,user)
