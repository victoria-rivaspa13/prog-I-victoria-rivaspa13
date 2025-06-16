def input_and_print():
    a = input("Ingrese el primer texto: ")
    b = input("Ingrese el segundo texto: ")
    c = input("Ingrese el tercer texto: ")

    return f"{a.upper()} {b.lower()} {c[0].upper() + c[1:]}"

resultado = input_and_print()

print(resultado)
