books = [
    # ISBN, TITLE, AUTHOR, AVAILABLE, CHECKOUT_NUM
    ["9788498386561", "Harry Potter", "Rowling", False, 2],
    ["9788493806125", "Don Quijote", "Cervantes", True, 0]
]

users = [
    # DNI, NAME, NUMBER_OF_CHECKOUTS, NUMBER_OF_CHECKINS
    [12345678, "Alice", 3, 2],
    [98765432, "Bob", 5, 1]
]

checked_out_books = [
    # ISBN, DNI, DUE_DATE
    ["9788498386561", 12345678, "1/10/2023"],
    ["9788498386561", 12345678, "23/10/2023"]
]

checked_in_books = [
    # ISBN, DNI, RETURNED_DATE
    ["9788498386561", 12345678, "1/10/2023"]
]

def add_book(titulo, apellido, ISBN):
    for book in books:
        if book[0] == ISBN:
            return
    books.append([ISBN, titulo, apellido, True, 0])
    return books

def list_all_books():
    for book in books:
        print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}")

def check_out_book(ISBN, DNI, fecha):
    book_exists = False
    for book in checked_out_books:
        if book[0] == ISBN:
            book_exists = True
        if not book_exists:
            return f"Unable to find the data for the values: ISBN {ISBN} and DNI: {DNI}"

    user_exists = False
    for user in users:
        if user[0] == DNI:
            user_exists = True
        if not user_exists:
            return f"Unable to find the data for the values: ISBN {ISBN} and DNI: {DNI}"

    for book in books:
        if book[0] == ISBN and not book[3]:
            return f"Book {ISBN} is not available"

    checked_out_books.append([ISBN, DNI, fecha])
    for book in books:
        if book[0] == ISBN:
            book[3] = False
            book[4] += 1
    for user in users:
        if user[0] == DNI:
            user[2] += 1
    return f"User {DNI} checked out book {ISBN}"


def check_in_book(ISBN):
    book_exists = False
    for book in books:
        if book[0] == ISBN:
            book_exists = True
    if not book_exists:
        return f"Book {ISBN} is not available"

    book_checked_out = False
    for record in checked_out_books:
        if record[0] == ISBN:
            book_checked_out = True
            DNI = record[1]
            checked_out_books.remove(record)
    if not book_checked_out:
        return f"Book {ISBN} is not available"

    for book in books:
        if book[0] == ISBN:
            book[3] = True
    for user in users:
        if user[0] == DNI:
            user[3] += 1

    return f"Book {ISBN} has been checked in"


