import sys
from stats import count_words
from stats import count_letters

def get_book_text(book_path):
    with open(book_path) as r:
        return r.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    letter_count = count_letters(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for lc in letter_count:
        print(f"{lc["char"]}: {lc["num"]}")
    print("============= END ===============")
main()
