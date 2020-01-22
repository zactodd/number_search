import random

DIRECTIONS = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
    "NE": (-1, 1),
    "SE": (1, 1),
    "SW": (1, -1),
    "NW": (-1, -1)
}


def generate_grid(height, width):
    """
    Generates a hxw of arrays of random single digit integers [[ int, ..., int ], ..., [...]].
    :param height: The height of the grid.
    :param width: The width of the grid.
    :return: 
    """
    return [[random.randint(0, 9) for _ in range(width)] for _ in range(height)]


def position_restrictions(word_len, height, width):
    """
    GEt the range in which each word can start from given it direction.
    :param word_len: The length of the words to be place in the grid.
    :param height: The height of the grid.
    :param width: The width of the grid.
    :return: A dictionary that evaluates to direction to the valid placement range.
    """
    return {
        "N": ((word_len - 1, height - 1), (0, width - 1)),
        "E": ((0, height - 1), (0, width - word_len - 1)),
        "S": ((0, height - word_len - 1), (0, width - 1)),
        "W": ((0, height - 1), (word_len - 1, width - 1)),
        "NE": ((word_len - 1, height - 1), (0, width - word_len - 1)),
        "SE": ((0, height - word_len - 1), (0, width - word_len - 1)),
        "SW": ((0, height - word_len - 1), (word_len - 1, width - 1)),
        "NW": ((word_len - 1, height - 1), (word_len - 1, width - 1)),
    }


def pprint_grid(grid):
    """
    Pretty prints the grid.
    :param grid: 
    """
    print("\n".join(" ".join(str(r) for r in g) for g in grid))


def is_overlapping(word_positions, words_positions, n=2):
    """
    Checks if a word overlaps with another word for n characters.
    :param word_positions: The positions of the current word.
    :param words_positions: THe position for the words already chosen.
    :param n: The number of overlapping characters.
    :return: True if it does overlap of n characters otherwise False
    """
    assert n >= 2, "n needs to be grater than 2."
    return any(len(word_positions) - len(word_positions - w) >= n for w in words_positions)


def generate_words(num_words, word_len, grid, reject_func=is_overlapping):
    """
    Generates random words that are located in the specified grid.
    :param num_words: The number of words to generate.
    :param word_len: The length of the words to be place in the grid.
    :param grid:
    :param reject_func: rejects word based on its position and the existing word positions.
    :return: A list of words to that are located in the grid.
    """
    height, width = len(grid), len(grid[0])
    restrictions = position_restrictions(word_len, height, width)
    word_hashes = set()
    words_positions = []
    words = []
    while len(word_hashes) < num_words:
        cardinal = random.choice(list(restrictions.keys()))
        (min_h, max_h), (min_w, max_w) = restrictions[cardinal]
        x0, y0 = random.randint(min_h, max_h), random.randint(min_w, max_w)
        x, y = DIRECTIONS[cardinal]
        positions = [(x0 + x * i, y0 + y * i) for i in range(word_len)]
        if (word_hash := (cardinal, (x0, y0))) not in word_hashes \
                and not reject_func(p_set := set(positions), words_positions):
            words.append("".join(str(grid[x][y]) for x, y in positions))
            word_hashes.add(word_hash)
            words_positions.append(p_set)
    return words





