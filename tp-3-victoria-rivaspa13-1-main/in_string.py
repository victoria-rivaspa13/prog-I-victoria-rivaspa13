def check_vowels():
    nombre = input("Ingrese el nombre del usuario: ")
    nombre = nombre.lower()
    contiene_a = "a" in nombre
    contiene_e = "e" in nombre
    contiene_i = "i" in nombre
    contiene_o = "o" in nombre
    contiene_u = "u" in nombre
    print("Contiene a:", contiene_a)
    print("Contiene e:", contiene_e)
    print("Contiene i:", contiene_i)
    print("Contiene o:", contiene_o)
    print("Contiene u:", contiene_u)

check_vowels()