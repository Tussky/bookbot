from stats import count_words, letters_in_text


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


def pretty_print(dict_to_print):
    list_dicts = split_dict(dict_to_print)
    sorted_letters = list_dicts.sort(key=ret_count)
    return sorted_letters


def main():
    frankenstein_text = get_book_text("./books/frankenstein.txt")
    print(frankenstein_text)

    letter_counts = letters_in_text(frankenstein_text)

    # print(f"{count_words(frankenstein_text)} words found in the document")
    # print(letter_counts)

    #    print(f"split dict {split_dict(letter_counts)}")
    print("pretty list:", pretty_print(letter_counts), sep="\n")

    td = {"letter": "e", "count": 12}
    print(ret_count(td))


main()
