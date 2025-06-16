def suma(a, b):
    return a + b

def resta(c, d):
    return c - d

def multiplica(x, y):
    return x * y

def operar(num1, num2, num3, num4):
    resultado_suma = suma(num1, num2)
    resultado_resta = resta(num3, num4)
    resultado_final = multiplica(resultado_suma, resultado_resta)
    print("El resultado final es:", resultado_final)

operar(1, 2, 3, 4)

def operar_listas(lista_de_listas):
    for sublista in lista_de_listas:
        resultado_suma = suma(sublista[0], sublista[1])
        resultado_resta = resta(sublista[2], sublista[3])
        resultado_final = multiplica(resultado_suma, resultado_resta)
        print("El resultado final es:", resultado_final)
operar_listas([[1, 2, 3, 4, 5],[6, 7, 8, 9],[10, 11, 12, 13]])


def cargaPalabras(n):
    palabras = []
    for _ in range(n):
        palabra = input("Ingresa una palabra: ")
        palabras.append(palabra)

    print("Lista de palabras ingresadas:", palabras)

    max_length = max(len(palabra) for palabra in palabras)
    palabras_largas = [palabra for palabra in palabras if len(palabra) == max_length]

    return palabras_largas[0] if len(palabras_largas) == 1 else palabras_largas



agenda = {}

def agendar(nombre, telefono):
    if nombre in agenda:
        respuesta = input(f"El contacto '{nombre}' ya existe. ¿Deseas actualizar el teléfono? (si/no): ")
        if respuesta.lower() == "si":
            agenda[nombre] = telefono
            print(f"El teléfono de '{nombre}' ha sido actualizado.")
        else:
            print("No se realizó ninguna actualización.")
    else:
        agenda[nombre] = telefono
        print(f"Nuevo contacto '{nombre}' agendado con éxito.")

#PRÁCTICA JUAN LONGO

def sum_of_expenses_by_type(expenses):
    res = {}
    for k, v in expenses.items():
        for t, exp in expenses.items():
            if t in res:
                res[t] += exp
            else:
                res[t] = exp
    return res


