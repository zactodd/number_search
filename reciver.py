import imaplib
import time
import json
from exceptions import assert_login


def gmail_matches(uid_search_str, login_key="key.json", username=None, password=None):
    """
    Get the unseen emails from given credentials.
    :param uid_search_str: uid formated search string.
    :param login_key: a json file containing the username and password information.
    :param username: the username if not none and :param password is also not none.
    :param password: the password if not none and :param username is also not none.
    :return
    """
    assert_login(username, password)
    with open(login_key, "r") as f:
        data = json.load(f)
        username, password = data["username"], data["password"]

    server = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    server.login(username, password)
    server.select('INBOX')
    _, data = server.uid('search', None, uid_search_str)

    results = []
    for s in data[0].split():
        _, full_data = server.uid('fetch', str(s.decode("utf-8")), '(RFC822)')
        results.append(full_data)
    server.logout()
    return results if len(results) > 0 else None


def listen_for_gmail(uid_search_str, login_key="key.json", username=None, password=None, wait=60):
    """
    Genertor for looking for emails
    :param uid_search_str: uid formated search string.
    :param login_key: a json file containing the username and password information.
    :param username: the username
    :param password: the password
    """
    while True:
        emails = gmail_matches(uid_search_str, login_key, username, password)
        if emails is not None:
            yield emails
        time.sleep(wait)

