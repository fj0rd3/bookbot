import sys
from stats import count_words, count_chars, sort_dict


def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()


def print_sorted_report(sorted_dict, book_text):
    str = f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {count_words(book_text)} total words
--------- Character Count -------
"""
    for dic in sorted_dict:
        if dic["char"].isalpha():
            str += f"{dic['char']}: {dic['num']}\n"
    str += "============= END ==============="
    return str


def main():
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    # num_words = count_words(book_text)
    chars_dict = count_chars(book_text)
    sorted_dict = sort_dict(chars_dict)
    print_report = print_sorted_report(sorted_dict, book_text)
    print(print_report)


main()
