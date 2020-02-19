from number_search import *
from docxtpl import DocxTemplate
import datetime


def number_search_doc(outfile, height=14, width=20, cols=3, num_words=33, word_len=7):
    """
    Creates a number search puzzle.
    :param outfile: The file to out the puzzle.
    :param height: height of the number search grid.
    :param width: height of the number search grid.
    :param cols: number of columns the number search has.
    :param num_words: the number of words in the number search.
    :param word_len: the length of the words in the number search.
    """
    # TODO add assertion restrictions.
    grid = generate_grid(height, width)
    formatted_grid = [{"cols": r} for r in grid]
    words = sorted(generate_words(num_words, word_len, grid))
    rows = num_words // cols
    formatted_words = [{"cols": [words[i + rows * j] for j in range(cols)]} for i in range(rows)]
    doc = DocxTemplate("templates/number_search_template.docx")
    doc.render({'grid': formatted_grid,  'search_table': formatted_words})
    doc.save(outfile)


def create_searches(n, func, out_dir="output"):
    """
    Creates n search puzzles.
    :param n: The number of puzzles to create.
    :param func: The puzzle creation method.
    :param out_dir: The output directory.
    """
    for _ in range(n):
        func(out_dir + "/" + datetime.datetime.now().strftime("number_search_%Y%m%d_%H%M%S_%f.docx"))

