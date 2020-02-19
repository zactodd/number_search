from docxcompose.composer import Composer
from docx import Document as Document_compose
import os
import datetime


BOOK_PREFIX = "number_search_book_"
SEARCH_PREFIX = "number_search_"


def date_now_str(prefix="", suffix="", time_str="%Y%m%d_%H%M%S_%f"):
    return datetime.datetime.now().strftime(f"{prefix}{time_str}{suffix}")


def search_book_name():
    return date_now_str(BOOK_PREFIX, ".docx")


def search_name():
    return date_now_str(SEARCH_PREFIX, ".docx")


def merge_word_documents(indir, outfile=search_book_name(), add_page_break=True):
    first, *files = [f"{indir}/{f}" for f in os.listdir(indir) if f.endswith(".docx")]
    master = Document_compose(first)
    if add_page_break:
        master.add_page_break()
    composer = Composer(master)
    for i, f in enumerate(files):
        tmp = Document_compose(f)
        if add_page_break and i < len(files) - 1:
            tmp.add_page_break()
        composer.append(tmp)
    composer.save(f"{indir}/{outfile}")


