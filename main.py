#!/bin/python3

def main():
    book_path = "books/frankenstein.txt"
    book_content = openBook(book_path)
    word_count = getWordcount(book_content)
    print("The total word count is:\n")
    print(word_count)


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


main()
