from docxcompose.composer import Composer
from docx import Document as Document_compose
import os
import datetime


BOOK_PREFIX = "number_search_book_"
SEARCH_PREFIX = "number_search_"


def date_now_str(prefix="", suffix="", time_str="%Y%m%d_%H%M%S_%f"):
    """
    Gets a string containing the current time with a selected :param prefix and/or :param suffix.
    :param prefix: Added to the front of the time string
    :param suffix: Added at the end of the string.
    :param time_str: THe time string format.
    :return:
    """
    return datetime.datetime.now().strftime(f"{prefix}{time_str}{suffix}")


def search_book_name():
    """
    A time stamped string for number search books.
    :return:
    """
    return date_now_str(BOOK_PREFIX, ".docx")


def search_name():
    """
    A time stamped string for number searches.
    :return:
    """
    return date_now_str(SEARCH_PREFIX, ".docx")


def merge_word_documents(indir, outfile=search_book_name(), add_page_break=True, delete_merged_files=True):
    """
    Merge word documents.
    :param indir: THe directory where the documents are stored.
    :param outfile: THe outfile name of the word documents.
    :param add_page_break: flag for adding page breaks between documents.
    :param delete_merged_files: flag determining if the files merged files should be deleted.
    """
    files = [f"{indir}/{f}" for f in os.listdir(indir) if f.endswith(".docx")]
    first, *rest = files
    master = Document_compose(first)
    if add_page_break:
        master.add_page_break()
    composer = Composer(master)
    for i, f in enumerate(rest):
        tmp = Document_compose(f)
        if add_page_break and i < len(rest) - 1:
            tmp.add_page_break()
        composer.append(tmp)
    composer.save(f"{indir}/{outfile}")

    if delete_merged_files:
        for f in files:
            os.remove(f)
