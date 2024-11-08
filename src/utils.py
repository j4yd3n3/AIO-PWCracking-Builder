import os
import sys
import src.leet
import src.append
import src.prepend
import src.toggles



#Function will take in an argument which is the filename and return a set of the contents inside of that file
def read_file_to_set(filename):
    lines_set = set()
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip whitespace from the beginning and end of the line and add it to the set
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
        # Add more elif conditions for other options
        elif option == 4:
            created_set.update(src.append.append_uno(created_set))
        elif option == 5:
            created_set.update(src.append.append_dos(created_set))
        elif option == 6:
            created_set.update(src.append.append_tres(created_set))
        elif option == 7:
            created_set.update(src.append.append_digit(created_set))
            print(options)
            print(f"After option 7 (append 1 digit), set size: {len(created_set)}")
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
            print(options)
            created_set.update(src.prepend.prepend_digit(created_set))
        elif option == 14:
            created_set.update(src.prepend.prepend_2digit(created_set))
        elif option == 15:
            created_set.update(src.prepend.prepend_3digit(created_set))

    return created_set


# Function to make sure the correct # of arguments are provided
#def check_file():
"""if len(sys.argv) < 3:
    print("Usage: python crack.py <path/to/your/list.txt> <path/to/desired/save/path.txt>")
    sys.exit(1)
else:
    file_path = sys.argv[1]
    output_file_path = sys.argv[2]    
    unique_lines = read_file_to_set(file_path)
    for line in unique_lines:
        print(line)"""
