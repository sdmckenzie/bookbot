#!/bin/python3

def main():
    book_path = "books/frankenstein.txt"
    book_content = openBook(book_path)

    print(book_content)


def openBook(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


main()
