from itertools import product

def toggle(orig: set) -> set:
    total_combinations = 0
    toggles_combinations = set()
    for word in orig:
        # Create a list where each character has both lowercase and uppercase options
        char_options = [[char.lower(), char.upper()] for char in word]

        # Generate all combinations of casing
        for combination in product(*char_options):
            toggled_word = ''.join(combination)
            toggles_combinations.add(toggled_word)
            total_combinations += 1

    # Uncomment the following line to see how many combinations were created
    print("\nTotal combinations generated:", total_combinations)
    return toggles_combinations

#Testing
# test_set = {"EasterEgg"}
# print(toggle(test_set))
# print(len(toggle(test_set)))