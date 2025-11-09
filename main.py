# Define initial function
import sys


def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents
# Inport stats from stats.py
from stats import count_words, count_characters
# Sort def
def sort_on(item):
    return item["num"]
# Format for new output(pretty text)
def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        # Exit with code 1 to indicate an error
        sys.exit(1)

    # The second item in sys.argv is the path to the book
    book_path = sys.argv[1]

    print("============== BOOKBOT ===============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count -----------")

    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars_dict = count_characters(book_text)
        # pretty print 
    print(f"Found {num_words} total words")
    print("----------- Character Count -------")

    # Convert dict to list of dicts for sorting 
    chars_list = []
    for char, num in chars_dict.items():
            #alpha chars only 
            if char.isalpha():
                 chars_list.append({"char": char, "num": num})

    # Sort in descending order by "num"
    chars_list.sort(reverse=True, key=sort_on)

    # Print each character and count
    for item in chars_list:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()