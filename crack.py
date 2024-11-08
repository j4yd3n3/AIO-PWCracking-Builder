import os
import sys
import src.leet
import src.append
import src.prepend
import src.toggles
import src.utils

def greeting(output_file):
    print("###########################################################")
    print("#               All-in-One PW List Formatter             #")
    print("###########################################################")
    print("\nChoose your options for modifying your list, one at a time.")
    print("Note: The order you select the options will be the order in which modifications are applied.")
    print("\nAvailable Options:")
    print(" 1. Basic Leet")
    print(" 2. Toggles/Cases")
    print(" 3. Expand Spaces\n")
    print(" 4. Append 1 Char")
    print(" 5. Append 2 Chars")
    print(" 6. Append 3 Chars\n")
    print(" 7. Append 1 Digit")
    print(" 8. Append 2 Digit")
    print(" 9. Append 3 Digit\n")
    print("10. Prepend 1 Char")
    print("11. Prepend 2 Chars")
    print("12. Prepend 3 Chars\n")
    print("13. Prepend 1 Digit")
    print("14. Prepend 2 Digit")
    print("15. Prepend 3 Digit")

    print("\nType 's' at any time to start list generator.\n")
    user_options = []
    while True:
        user_input = input("Enter an option number (e.g., 1, 2, 3) or 's' to start list generator: ")
        if user_input.lower() == 's':
            print(f"Saving updated list to {output_file}")
            break
        try:
            option = int(user_input)
            if option in range(1, 16):
                user_options.append(option)
                print(f"Option {option} added.")
                print("Current selected options:", user_options)
            else:
                print("Invalid option. Please enter a number between 1 and 15.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    return user_options  

def write_set_to_file(output_file_path, modified_set):
    try:
        with open(output_file_path, 'w') as file:
            for item in modified_set:
                file.write(f"{item}\n")
        print(f"Successfully wrote {len(modified_set)} entries to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    orig_set = set()
    if len(sys.argv) < 3:
        print("Usage: python crack.py <path/to/your/list.txt> <path/to/desired/save/path.txt>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        orig_set = src.utils.read_file_to_set(file_path)

    user_options = greeting(output_file_path)
    modified_set = src.utils.create_set(orig_set, user_options)
    write_set_to_file(output_file_path, modified_set)

if __name__ == '__main__':
    main()
