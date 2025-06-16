expenses = [
    ["Juan", 1345, "Supermercado"],
    ["Pancho", 2000, "Nafta"],
    ["Juan", 1200, "Dentista"],
    ["Agustin", 1000, "Supermercado"]
]

def extract(expenses):
    nombres = []
    categorias = []
    for i in range(len(expenses)):
        if expenses[i][0] not in nombres:
            nombres.append(expenses[i][0])
        if expenses[i][2] not in categorias:
            categorias.append(expenses[i][2])

    return nombres, categorias

def transform_total_person(expenses):
    total_per = {}
    for expense in expenses:
        nombre, monto = expense[0], expense[1]
        if nombre not in total_per:
            total_per[nombre] = 0
        total_per[nombre] += monto
    return total_per

def transform_total_category(expenses):
    total_cat = {}
    for expense in expenses:
        categoria, monto = expense[2], expense[1]
        if categoria not in total_cat:
            total_cat[categoria] = 0
        total_cat[categoria] += monto
    return total_cat

def get_max_gasto(expenses):
    max_gasto = 0
    max_key = None
    for key, value in expenses.items():  # Iterar sobre las claves y valores
        if value > max_gasto:
            max_gasto = value
            max_key = key
    return max_key, max_gasto

def load(expenses):
    nombres, categorias = extract(expenses)
    total_per = transform_total_person(expenses)
    total_cat = transform_total_category(expenses)
    max_gasto_persona = get_max_gasto(total_per)
    max_gasto_cat = get_max_gasto(total_cat)
    print("Nombres:", nombres)
    print("Categorías:", categorias)
    print("Total por persona:", total_per)
    print("Total por categoría:", total_cat)
    print("Persona con más gasto:", max_gasto_persona)
    print("Categoría con más gasto:", max_gasto_cat)

load(expenses)
