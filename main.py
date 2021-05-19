from Bot.bot import *


def update_db(thread_text, user):
    return


if __name__ == '__main__':
    auth_api = authenticate()
    while True:
        last_seen_id = get_last_seen_id()
        last_seen_id, status_id, author_id, user = get_mentioned_thread(auth_api, last_seen_id)
        if last_seen_id == 0 and status_id == 0 and author_id == 0 and user == 0:
            continue
        set_last_seen_id(last_seen_id)
        thread = get_thread_text(auth_api, author_id, status_id)
        update_db(thread, user)
