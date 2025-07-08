def count_words(text):
    return len(text.split())


def split_words(text):
    return len(text.split())


def count_letters(text):
    letter_dict = {}

    for letter in text:
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] = letter_dict[letter] + 1
        else:
            letter_dict[letter] = 1

    return letter_dict
