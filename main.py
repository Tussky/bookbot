import sys

from stats import count_letters, count_words


def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents


def split_dict(dict_to_sort):
    list_of_dicts = []
    for pair in dict_to_sort.items():
        temp_dict = {}
        temp_dict["letter"] = pair[0]
        temp_dict["count"] = pair[1]
        list_of_dicts.append(temp_dict)

    return list_of_dicts


def ret_count(given_dict):
    return given_dict["count"]


def sort_letter_counts(dict_to_print):
    list_dicts = split_dict(dict_to_print)
    list_dicts.sort(key=ret_count, reverse=True)
    return list_dicts


def report(filepath):
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    pretty_letter_counts = sort_letter_counts(count_letters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(
        "----------- Word Count ----------", f"Found {word_count} total words", sep="\n"
    )
    print("--------- Character Count -------", sep="\n")

    for letter_count in pretty_letter_counts:
        if letter_count["letter"].isalpha():
            print(f"{letter_count["letter"]}: {letter_count["count"]}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Incorrect input structure!")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    report(sys.argv[1])


main()

