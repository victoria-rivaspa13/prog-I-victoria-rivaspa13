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

# 1. Gestión de Libros

def add_book(title, author, isbn):
    """Agrega un libro nuevo a la biblioteca."""
    for book in books:
        if book[0] == isbn:
            return  # El ISBN ya existe, no se hace nada.
    books.append([isbn, title, author, True, 0])  # El libro se agrega como disponible.

def list_all_books():
    """Imprime todos los libros registrados en la biblioteca."""
    for book in books:
        print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}")

# 2. Gestión de Préstamos

def check_out_book(isbn, dni, checkout_date):
    """Permite prestar un libro a un usuario registrado."""
    # Verificar si el ISBN existe en la biblioteca
    book = next((b for b in books if b[0] == isbn), None)
    if not book:
        return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # Verificar si el DNI existe en los usuarios
    user = next((u for u in users if u[0] == dni), None)
    if not user:
        return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # Verificar si el libro está disponible
    if not book[3]:  # Disponible = True
        return f"Book {isbn} is not available"

    # Registrar el préstamo
    book[3] = False  # Marcar como no disponible
    book[4] += 1  # Incrementar el contador de préstamos del libro
    user[2] += 1  # Incrementar el contador de préstamos del usuario
    checked_out_books.append([isbn, dni, checkout_date])
    return f"User {dni} checked out book {isbn}"

def check_in_book(isbn):
    """Permite devolver un libro prestado."""
    # Verificar si el ISBN existe en la biblioteca
    book = next((b for b in books if b[0] == isbn), None)
    if not book:
        return f"Book {isbn} is not available"

    # Verificar si el libro está en préstamo
    checked_out = next((c for c in checked_out_books if c[0] == isbn), None)
    if not checked_out:
        return f"Book {isbn} is not available"

    # Registrar la devolución
    book[3] = True  # Marcar como disponible
    checked_out_books.remove(checked_out)  # Eliminar de los préstamos
    user = next((u for u in users if u[0] == checked_out[1]), None)
    if user:
        user[3] += 1  # Incrementar el contador de devoluciones del usuario
    checked_in_books.append([isbn, checked_out[1], "Fecha de hoy"])  # Registrar devolución
    return f"Book {isbn} checked in successfully"

