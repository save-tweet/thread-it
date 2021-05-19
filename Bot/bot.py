import tweepy

file_name = 'last_seen_id.txt'


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
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def set_last_seen_id(last_seen_id, ):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
