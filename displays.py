from number_search import *
from docxtpl import DocxTemplate
import datetime
import time
import jinja2


def number_search_doc(outfile):
    """
    Creates a number search puzzle.
    :param outfile: The file to out the puzzle.
    """
    height, width, num_words, word_len = 14, 20, 56, 7
    grid = generate_grid(height, width)
    formatted_grid = [{"cols": r} for r in grid]
    words = sorted(generate_words(num_words, word_len, grid))
    rows = num_words // 4
    formatted_words = [{"cols": [words[i + rows * j] for j in range(4)]} for i in range(rows)]
    doc = DocxTemplate("templates/number_search_template.docx")
    doc.render({'grid': formatted_grid,  'search_table': formatted_words})
    doc.save(outfile)
    print(outfile)


def create_searches(n, func, out_dir="output"):
    """
    Creates n search puzzles.
    :param n: The number of puzzles to create.
    :param func: The puzzle creation method.
    :param out_dir: The output directory.
    """
    for _ in range(n):
        func(out_dir + "/" + datetime.datetime.now().strftime("number_search_%Y%m%d_%H%M%S_%f.docx"))
