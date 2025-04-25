import os
import sys
import src.leet
import src.append
import src.prepend
import src.toggles
import src.expand


def read_file_to_set(filename):
    lines_set = set()
    try:
        with open(filename, 'r') as file:
            for line in file:
                lines_set.add(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    return lines_set


def create_set(orig_set: set, options: list) -> set:
    created_set = orig_set.copy()
    for option in options:
        if option == 1:
            created_set.update(src.leet.leet(created_set))
        elif option == 2:
            created_set.update(src.toggles.toggle(created_set))
        elif option == 3:
            created_set.update(src.expand.expand_spaces(created_set))
        elif option == 4:
            created_set.update(src.append.append_uno(created_set))
        elif option == 5:
            created_set.update(src.append.append_dos(created_set))
        elif option == 6:
            created_set.update(src.append.append_tres(created_set))
        elif option == 7:
            created_set.update(src.append.append_digit(created_set))
        elif option == 8:
            created_set.update(src.append.append_2digit(created_set))
        elif option == 9:
            created_set.update(src.append.append_3digit(created_set))
        elif option == 10:
            created_set.update(src.prepend.prepend_uno(created_set))
        elif option == 11:
            created_set.update(src.prepend.prepend_dos(created_set))
        elif option == 12:
            created_set.update(src.prepend.prepend_tres(created_set))
        elif option == 13:
            created_set.update(src.prepend.prepend_digit(created_set))
        elif option == 14:
            created_set.update(src.prepend.prepend_2digit(created_set))
        elif option == 15:
            created_set.update(src.prepend.prepend_3digit(created_set))
        elif option == 16:
            created_set.update(src.expand.expand_spaces(created_set))
            created_set.update(src.leet.leet(created_set))
            created_set.update(src.toggles.toggle(created_set))
        elif option == 17:
            created_set.update(
            src.combinator.combine(
            created_set,
            min_parts=2,
            max_parts=2,
            separators=[""],
            max_length=32
        ))
        elif option == 18:
            delimiter = input("Enter the custom delimiter: ")
            created_set.update(src.append.append_custom(created_set, delimiter))



    return created_set
