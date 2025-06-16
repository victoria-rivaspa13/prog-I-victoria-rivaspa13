texto = input("Ingrese un texto: ")

primera_letra = texto[0].lower()
ultima_letra = texto[-1].lower()
anteultima_letra = texto[-2].lower()
primera_letra_neg = texto[-len(texto)].lower()

print(primera_letra)
print(ultima_letra)
print(anteultima_letra)
print(primera_letra_neg)