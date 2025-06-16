def debug(a):
    b = "orange"
    if len (a) > 3:
        b = a + " " + b
        if a == "apple":
            b = b.replace("a", "x")
        if a[-1] == "e":
            b = b[::2]
        if len(b) % 2 == 0:
            b = b[:-1]
        else:
            b = a + b
    else:
        b = a[0:1] + " " + b[1:2:1]
    print(f"Resultado: {b}")
debug("apple")

def get_consonants(texto):
    nuevo_string = ""
    impares = texto[::1]
    vocales = "aeiou"
    if impares not in vocales:
        nuevo_string = impares
    else:
        nuevo_string = impares - vocales
    return nuevo_string
print(get_consonants("programacion"))

def has_more_as(string):
    tiene_a = "a" in string
    no_a = string [::] != "a"
    cantidad_a = len(tiene_a)
    cantidad_not_a = len(no_a)
    if cantidad_a >= cantidad_not_a:
        return True
    else:
        return False
has_more_as("banana")

def car_condition():
    kilometros = int(input("Ingrese el número de kilómetros recorridos por el coche: "))
    puntos = 0
    if kilometros <= 20.000:
        puntos = 0.5 * kilometros
    elif kilometros > 20.000:
        km_restantes = kilometros - 20.000
        puntos_despues_de_veinte = 0.2 * km_restantes
        puntos = 10.000 + puntos_despues_de_veinte
    return puntos
car_condition(30.000)