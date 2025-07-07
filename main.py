from stats import count_words, letters_in_text


def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents


def main():
    frankenstein_text = get_book_text("./books/frankenstein.txt")
    print(frankenstein_text)

    letter_counts = letters_in_text(frankenstein_text)

    print(f"{count_words(frankenstein_text)} words found in the document")
    print(letter_counts)


main()
