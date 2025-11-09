def count_words(text):
    # Split the text into words using split() and return how many there are
    words = text.split()
    return len(words)

def count_characters(text):
    # Convert the text to lowercase so that 'A' and 'a' count as the same
    text = text.lower()

    # Create an empty dictionary to store character counts
    char_count = {}

    # Loop through each character in the text
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count