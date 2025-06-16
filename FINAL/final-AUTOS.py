cars = [
    # PLATE, MODEL, BRAND, AVAILABLE, RENT_COUNT
    ["ABC123", "Model S", "Tesla", True, 3],
    ["XYZ987", "Corolla", "Toyota", False, 5],
]

customers = [
    # DNI, NAME, RENTED_CARS, RETURNED_CARS
    [12345678, "Alice", 2, 1],
    [98765432, "Bob", 1, 2],
]

rented_cars = [
    # PLATE, DNI, RENT_DATE
    ["XYZ987", 12345678, "2024-11-01"],
]

returned_cars = [
    # PLATE, DNI, RETURN_DATE
    ["ABC123", 98765432, "2024-10-30"],
]

def add_car(matricula, modelo, marca):
    cars.append([matricula, modelo, marca, True, 0])

def list_cars():
    for car in cars:
        if car[3]:
            print(f"Matricula: [{car[0]}, Modelo: {car[1]}, Marca: {car[2]}]")

def alquilar(matricula, dni, fecha):
    cliente_encontrado = None
    auto_encontrado = None

    for cliente in customers:
        if cliente[0] == dni:
            cliente_encontrado = cliente

    for car in cars:
        if car[0] == matricula:
            auto_encontrado = car

    if not cliente_encontrado or not auto_encontrado:
        return f"Imposible encontrar data para la matricula:{matricula} y el DNI: {dni}"

    if not auto_encontrado[3]:
        return f"Auto:{matricula} no disponible"

    auto_encontrado[3] = False
    auto_encontrado[4] += 1
    cliente_encontrado[2] += 1
    rented_cars.append([matricula, dni, fecha])
    return f"El cliente: {dni} rentó el auto: {auto_encontrado}"

def devolver(matricula, dni):
    renta_encontrada = None
    auto_encontrado = None
    for car in cars:
        if car[0] == matricula:
            auto_encontrado = car

    for renta in rented_cars:
        if renta[0] == matricula:
            renta_encontrada = renta

    if not renta_encontrada or not auto_encontrado:
        return f"El auto {matricula} no disponible"

    auto_encontrado[3] = True
    returned_cars.append([renta_encontrada[0], renta_encontrada[1], "today"])
    rented_cars.remove(renta_encontrada)
    for cliente in customers:
        if cliente[0] == renta_encontrada[1]:
            cliente[3] += 1


