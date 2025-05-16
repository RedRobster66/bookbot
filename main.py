import sys
from stats import get_num_words     
from stats import get_chars_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")  # Print usage message
    sys.exit(1)  # Exit with status code 1

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents

def main():
#    book_path = 'books/frankenstein.txt'  # relative path to the book file
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}')
    print('----------- Word Count ----------')
    count = get_num_words(book_contents)
    print(f'Found {count} total words')
    print('--------- Character Count -------')
    sorted_counts = get_chars_count(book_contents)
    for char, freq in sorted_counts:
        print(f"{char}: {freq}")
    
    print('============= END ===============')

if __name__ == '__main__':
    main()
