def how_many(string, letra):
    suma = 0
    for char in string:
        if char == letra:
            suma += 1
    return suma

print(how_many("Seguramente esta frase es suficientemente util", "s"))

def xpenses(tupla):
    gastos_agrupados = dict()
    for gasto, monto in tupla:
        for num in monto:
            suma_low = 0
            suma_med = 0
            suma_hi = 0
            if num <= 100:
                suma_low += num
                gastos_agrupados[low] = suma_low
            elif num > 100 and num <= 500:
                suma_med += num
                gastos_agrupados[med] = suma_med
            else:
                suma_hi += num
                gastos_agrupados[hi] = suma_hi
        return gastos_agrupados

gastos = (
    ("comida", [50, 150, 700]),
    ("transporte", [20, 300, 800]),
    ("entretenimiento", [60, 400, 1000])
)
print(xpenses(gastos))

def unique_letters(lista):
    resultado = []
    for palabra in lista:
        for letra in palabra:
            if letra in resultado:
                letra += 1
            else:
                resultado.append(letra)
    return resultado
print(unique_letters(palabras = ["mesa", "cama", "lapicera"]))

