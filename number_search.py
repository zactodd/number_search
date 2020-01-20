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

    
def generate_words(num_words, word_len, grid):
    """
    Generates random words that are located in the specified grid.
    :param num_words: The number of words to generate.
    :param word_len: The length of the words to be place in the grid.
    :param grid: 
    :return: A list of words to that are located in the grid.
    """
    height, width = len(grid), len(grid[0])
    restrictions = position_restrictions(word_len, height, width)
    word_hashes = set()
    words = []
    while len(word_hashes) < num_words:
        cardinal = random.choice(list(restrictions.keys()))
        (min_h, max_h), (min_w, max_w) = restrictions[cardinal]
        x0, y0 = random.randint(min_h, max_h), random.randint(min_w, max_w)
        if (word_hash := (cardinal, (x0, y0))) not in word_hashes:
            x, y = DIRECTIONS[cardinal]
            words.append("".join(str(grid[x0 + x * i][y0 + y * i]) for i in range(word_len)))
            word_hashes.add(word_hash)
    return sorted(words)






