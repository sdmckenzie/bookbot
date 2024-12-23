#!/bin/python3

def main():
    book_path = "books/frankenstein.txt"
    book_content = openBook(book_path)
    word_count = getWordcount(book_content)
    print("The total word count is:\n")
    print(word_count)

    characters = countCharacters(book_content)
    print(characters)


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


main()
