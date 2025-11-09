def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import count_characters


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    chars = count_characters(book_text)
    print(f"Found {num_words} total words")
    print(chars)


if __name__ == "__main__":
    main()