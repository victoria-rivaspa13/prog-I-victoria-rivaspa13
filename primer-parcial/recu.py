def debug(a):
    b = a * 2
    if b % 2 == 0:
        b = b + 1
    else:
        b = a // 2
    c = a + b
    print (f"Resultado final: {c}")

def number():
    num = float(input("Ingrese un numero: "))
    if num % 2 == 0 and num != 0:
        print(f"El numero {num} es par")
    elif num == 0:
        print(f"El numero {num} es cero")
    else:
        print(f"El numero {num} es impar")
number()
def similar_string(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    largo_1 = len(s1)
    largo_2 = len(s2)
    vocales_1 = s1.count("a") + s1.count("e") + s1.count("i") + s1.count("o") + s1.count("u")
    vocales_2 = s2.count("a") + s2.count("e") + s2.count("i") + s2.count("o") + s2.count("u")
    if largo_1 == largo_2:
        if vocales_1 == vocales_2:
            if s1[0] == s2[0]:
                if s1[-1] == s2[-1]:
                    return True

    return False
print(similar_string("",""))
def is_at_beginning(frase):
    letra = input("Ingrese una letra: ")
    mitad = len(frase) // 2
    primera_mitad = frase[:mitad + 1]
    cantidad_a = primera_mitad.count(letra)
    if cantidad_a > 2:
        return True
    else:
        return False
print(is_at_beginning("Para aprobar hay que estudiar"))

