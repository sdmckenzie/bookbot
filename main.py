#!/bin/python3

def main():
    book_path = "books/frankenstein.txt"
    book_content = openBook(book_path)
    word_count = getWordcount(book_content)
    print(f"--- Begin report of {book_path} ---")
    print(f"The total word count is: {word_count}\n")

    characters = countCharacters(book_content)
    # print(characters)
    printReport(characters)


def openBook(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def getWordcount(document):
    word_list = document.split()
    counter = 0
    for word in word_list:
        counter += 1
    return counter


def countCharacters(document):
    lower_case_string = document.lower()
    char_count = {}
    for char in lower_case_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def printReport(char_dict):
    sorted_dict = dict(
        sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    for entry in sorted_dict:
        if entry.isalpha():
            print(f"The {entry} character was found {char_dict[entry]} times")
        else:
            pass


main()
