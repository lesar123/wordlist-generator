import itertools


def generate_wordlist(chars, min_length, max_length, output_file, limit=None, chunk_size=100000):
    """
    Generate a wordlist and save to a file efficiently.

    :param chars: A string of characters to include in the wordlist
    :param min_length: Minimum length of words
    :param max_length: Maximum length of words
    :param output_file: File to save the wordlist
    :param limit: Maximum number of words to save in the file
    :param chunk_size: Number of words to process before writing to the file
    """
    count = 0  # Track the number of words written
    buffer = []  # Temporary storage for bulk writing

    with open(output_file, 'w') as f:
        for length in range(min_length, max_length + 1):
            for combination in itertools.product(chars, repeat=length):
                if limit and count >= limit:
                    if buffer:  # Write any remaining words in the buffer
                        f.write('\n'.join(buffer) + '\n')
                    print(f"Reached the limit of {limit} words. Stopping generation.")
                    return

                word = ''.join(combination)

                # Skip patterns like leading '0000'
                if word.startswith('0000'):
                    continue

                # Add word to buffer
                buffer.append(word)
                count += 1

                # Write buffer to file if it reaches the chunk size
                if len(buffer) >= chunk_size:
                    f.write('\n'.join(buffer) + '\n')
                    buffer = []  # Clear the buffer

        # Write any remaining words in the buffer
        if buffer:
            f.write('\n'.join(buffer) + '\n')

    print(f"Generated {count} words in total. Wordlist saved to {output_file}.")


def collect_inputs():
    """
    Collect and combine multiple inputs for the character set.

    :return: Combined character set
    """
    chars = ""

    # Add numbers
    if input("Include numbers (0-9)? (yes/no): ").strip().lower() == 'yes':
        chars += "0123456789"

    # Add lowercase letters
    if input("Include lowercase letters (a-z)? (yes/no): ").strip().lower() == 'yes':
        chars += "abcdefghijklmnopqrstuvwxyz"

    # Add uppercase letters
    if input("Include uppercase letters (A-Z)? (yes/no): ").strip().lower() == 'yes':
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Add special characters
    if input("Include special characters (!@#$%^&* etc.)? (yes/no): ").strip().lower() == 'yes':
        chars += "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    # Add custom inputs
    print("Add custom inputs (e.g., names, phrases). Type 'done' when finished.")
    while True:
        custom_input = input("Custom input: ").strip()
        if custom_input.lower() == 'done':
            break
        chars += custom_input

    # Check if the input set is empty
    if not chars:
        print("Error: No characters provided for the wordlist.")
        exit(1)  # Exit the program if the input is empty

    return chars


def main():
    print("Optimized Wordlist Generator")

    # Collect inputs for the character set
    chars = collect_inputs()
    print(f"\nFinal character set: {chars}")

    # Get wordlist generation parameters
    min_length = int(input("Enter minimum word length: "))
    max_length = int(input("Enter maximum word length: "))
    output_file = input("Enter the output file name: ")
    limit = int(input("Enter the maximum number of words to generate (e.g., 1000): "))

    # Generate the wordlist
    print("\nGenerating wordlist...")
    generate_wordlist(chars, min_length, max_length, output_file, limit)
    print(f"Wordlist saved to {output_file}")


if __name__ == "__main__":
    main()