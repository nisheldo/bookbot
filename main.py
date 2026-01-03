from stats import *
import sys

def get_book_text(p):
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()

def main():

    if len(sys.argv) > 1:

        path = sys.argv[1]
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        get_num_words(get_book_text(path))
        print("--------- Character Count -------")
        report_list = dict_to_sorted_list(count_chars_in_string(get_book_text(path)))
        report_list.sort(key=lambda x: x[1], reverse=True)
        for f in report_list:
            print(f"{f[0]}: {f[1]}")
        print("============= END ===============")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()