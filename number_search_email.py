from reciver import listen_for_gmail
from sender import send_gmail_with_attachment
from displays import number_search_doc, create_searches
import shutil
import os

TMP_DIR = "tmp"


def reply_to_emails(wait=3600):
    for emails in listen_for_gmail('(UNSEEN SUBJECT "Numbersearch")', wait=wait):
        # TODO properly extra "from" data
        # TODO fix expecting cases.
        email_info = str(emails[0][0][1].decode("utf-8")).split("\r\n")
        try:
            from_address = next(i[i.index("<") + 1:i.index(">")] for i in email_info if len(i) > 6 and "From: " in i)
        except :
            continue

        shutil.rmtree(TMP_DIR)
        os.mkdir(TMP_DIR)
        create_searches(10, number_search_doc, TMP_DIR)
        shutil.make_archive("numbersearch", 'zip', "tmp")
        send_gmail_with_attachment("Numbersearch puzzles are attached.", "Numbersearch Puzzles", "numbersearch.zip",
                                   from_address)
        shutil.rmtree(TMP_DIR)
        os.remove("numbersearch.zip")


reply_to_emails(1)
