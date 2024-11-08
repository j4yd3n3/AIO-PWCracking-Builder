from itertools import product

leet_possibilities = {
    "a": ["4", "@"],
    "b": ["8", "6"],
    "c": ["<", "{", "("],
    "e": ["3"],
    "g": ["6", "9"],
    "h": ["#"],
    "i": ["1", "!"],
    "l": ["1", "!"],
    "o": ["0"],
    "q": ["9"],
    "s": ["5", "$", "z"],
    "t": ["7", "+"],
    "x": ["%"],
    "z": ["2"]
}
def leet(orig: set) -> set:
    leet_combinations = set() 
    for word in orig:
        char_options = []
        for char in word:
            if char.lower() in leet_possibilities:
                char_options.append([char] + leet_possibilities[char.lower()])
            else:
                char_options.append([char])

        for combination in product(*char_options):
            leet_word = ''.join(combination)
            leet_combinations.add(leet_word)  # Add each leet word to the set

    # Uncomment the following line to see how many combinations were created
    # print("\nTotal combinations generated:", len(leet_combinations))
    return leet_combinations

# Testing:
# test_set = {"Egg"}
# print(leet(test_set))
# print(type(leet(test_set)))
# print(len(leet(test_set)))
