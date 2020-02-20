from ns.reciver import listen_for_gmail
from ns.sender import send_gmail_with_attachment
from ns.displays import number_search_doc, create_searches
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
        except:
            continue

        if os.path.exists(TMP_DIR):
            shutil.rmtree(TMP_DIR)
        os.mkdir(TMP_DIR)

        create_searches(50, number_search_doc, TMP_DIR)
        shutil.make_archive("numbersearch", 'zip', TMP_DIR)
        send_gmail_with_attachment("Numbersearch puzzles are attached.", "Numbersearch Puzzles", "numbersearch.zip",
                                   from_address)
        shutil.rmtree(TMP_DIR)
        os.remove("numbersearch.zip")


if __name__ == '__main__':
    reply_to_emails(1)
