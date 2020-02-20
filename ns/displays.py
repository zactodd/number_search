from ns.number_search import *
from docxtpl import DocxTemplate
from ns import utils


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


def create_searches(n, func, outdir="output", merge=True):
    """
    Creates n search puzzles.
    :param n: The number of puzzles to create.
    :param func: The puzzle creation method.
    :param outdir: The output directory.
    :param merge: Flag representing if all the searches will be merged into one document after.
    """
    for _ in range(n):
        func(outdir + "/" + utils.search_name())

    if merge:
        utils.merge_word_documents(outdir)

