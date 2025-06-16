movies = [
    ["MV123", "Inception", "Christopher Nolan", True, 5],
    ["MV124", "Interstellar", "Christopher Nolan", False, 10],
]

users = [
    [12345678, "Alice", 2, 1],
    [98765432, "Bob", 1, 2],
]

rented_movies = [
    ["MV124", 12345678, "2024-11-01"],
]

returned_movies = [
    ["MV123", 98765432, "2024-10-30"],
]

def añadir(codigo, titulo, director):
    movies.append([codigo, titulo, director, True, 0])


def listar_disponibles():
    for pelicula in movies:
        if pelicula[3]:  # Verifica si está disponible
            print(f"Código: {pelicula[0]}, Título: {pelicula[1]}, Director: {pelicula[2]}")


def rentar_pelicula(codigo, dni, fecha):
    pelicula_encontrada = None
    usuario_encontrado = None

    # Buscar película
    for pelicula in movies:
        if pelicula[0] == codigo:
            pelicula_encontrada = pelicula

    # Buscar usuario
    for usuario in users:
        if usuario[0] == dni:
            usuario_encontrado = usuario

    # Validaciones
    if not pelicula_encontrada or not usuario_encontrado:
        return f"Datos no encontrados para código {codigo} y DNI {dni}"

    if not pelicula_encontrada[3]:  # Si no está disponible
        return f"La película {codigo} no está disponible"

    # Procesar renta
    pelicula_encontrada[3] = False
    pelicula_encontrada[4] += 1
    usuario_encontrado[2] += 1
    rented_movies.append([codigo, dni, fecha])
    return f"El usuario {dni} rentó la película {codigo}"


def devolver_pelicula(codigo):
    pelicula_encontrada = None
    renta_encontrada = None

    # Buscar película
    for pelicula in movies:
        if pelicula[0] == codigo:
            pelicula_encontrada = pelicula

    # Buscar renta
    for renta in rented_movies:
        if renta[0] == codigo:
            renta_encontrada = renta

    # Validaciones
    if not pelicula_encontrada or not renta_encontrada:
        return f"La película {codigo} no está registrada como rentada"

    # Procesar devolución
    pelicula_encontrada[3] = True
    rented_movies.remove(renta_encontrada)
    returned_movies.append([codigo, renta_encontrada[1], "today"])  # Fecha genérica "today"

    # Actualizar usuario
    for usuario in users:
        if usuario[0] == renta_encontrada[1]:
            usuario[3] += 1
            break

    return f"La película {codigo} ha sido devuelta correctamente"

if __name__ == "__main__":
    print("Películas disponibles:")
    listar_disponibles()

    print("\nAñadiendo nueva película...")
    añadir("MV125", "Dunkirk", "Christopher Nolan")
    listar_disponibles()

    print("\nRentando película MV123...")
    print(rentar_pelicula("MV123", 12345678, "2024-12-05"))

    print("\nIntentando devolver película MV124...")
    print(devolver_pelicula("MV124"))

    print("\nIntentando devolver película MV123...")
    print(devolver_pelicula("MV123"))
