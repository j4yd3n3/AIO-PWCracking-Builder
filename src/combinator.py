from itertools import permutations, product

DEFAULT_SEPARATORS = ["", "_", "-", "."]

def combine(words: set[str],
            min_parts: int = 2,
            max_parts: int = 2,
            separators: list[str] = DEFAULT_SEPARATORS,
            max_length: int | None = None) -> set[str]:

    combos = set()

    word_list = list(words)

    for parts in range(min_parts, max_parts + 1):
        for words_tuple in permutations(word_list, parts):
            for sep_tuple in product(separators, repeat=parts - 1):
                candidate = words_tuple[0]
                for w, sep in zip(words_tuple[1:], sep_tuple):
                    candidate += sep + w
                if max_length is None or len(candidate) <= max_length:
                    combos.add(candidate)
    return combos
