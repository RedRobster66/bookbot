def get_num_words(book_contents):
    count = len(book_contents.split())
    return count

def get_chars_count(text):
    text = text.lower()  # Convert text to lowercase
    char_counts = {}

    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char_counts[char] = char_counts.get(char, 0) + 1

    # Sort the dictionary by frequency in descending order
    sorted_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts