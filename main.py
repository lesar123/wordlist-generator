import itertools
import random


def wordlist_generate(wordlist, max_length, num_combinations):
    #Generate a specified number of randomized word combinations.

    combinations = []
    for _ in range(num_combinations):
        length = random.randint(1, max_length)  # Randomize the length for variety
        combo = ''.join(random.choices(wordlist, k=length))
        combinations.append(combo)
    return combinations


def options():
    #Function for creating a wordlist based on user inputs.

    wordlist = []  # Main wordlist

    # Add numbers
    number_choice = input("Do you want to add numbers from 0-9? (yes/no): ").strip().lower()
    if number_choice == 'yes':
        number = [str(num) for num in range(10)]
        wordlist.extend(number)

    # Add lowercase letters
    word_choice = input("Do you want to add letters from a-z? (yes/no): ").strip().lower()
    if word_choice == 'yes':
        letters = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
        wordlist.extend(letters)

        # Add uppercase letters
        uppercase_word_choice = input("Do you want to add uppercase letters from A-Z? (yes/no): ").strip().lower()
        if uppercase_word_choice == 'yes':
            uppercase_letters = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]
            wordlist.extend(uppercase_letters)

    # Add special characters
    special_char_choice = input("Do you want to add some special characters? (yes/no): ").strip().lower()
    if special_char_choice == 'yes':
        special_chars = [chr(char) for char in range(33, 48)] + \
                        [chr(char) for char in range(58, 65)] + \
                        [chr(char) for char in range(91, 97)]   + \
                        [chr(char) for char in range(123, 127)]
        wordlist.extend(special_chars)

    # Add custom inputs
    print("Do you have some special requirements (e.g., names)? Type 'stop' to finish.")
    while True:
        special_input = input("Add: ").strip()
        if special_input.lower() == 'stop':
            break
        wordlist.append(special_input)

    return wordlist


def main():
    print("This is the main program")
    max_length = int(input("Enter the maximum length for combinations: "))
    num_combinations = int(input("Enter the number of random combinations to generate: "))

    wordlist = options()  # Generate the wordlist based on user inputs

    print("\nGenerating random combinations...\n")
    combinations = wordlist_generate(wordlist, max_length, num_combinations)

    # Print the random combinations
    for combo in combinations:
        print(combo)


if __name__ == "__main__":
    main()