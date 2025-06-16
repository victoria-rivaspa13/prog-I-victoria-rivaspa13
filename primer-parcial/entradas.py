edad_adolescente = 14
edad_abuelo = 66

costo_adolescente = 0
costo_abuelo = 0

if 5 <= edad_adolescente <= 17:
    costo_adolescente = 50
elif 18 <= edad_adolescente <= 50:
    costo_adolescente = 30
else:
    costo_adolescente = 10

if edad_abuelo < 5:
    costo_abuelo = 0
elif 5 <= edad_abuelo <= 17:
    costo_abuelo = 50
elif 18 <= edad_abuelo <= 50:
    costo_abuelo = 30
else:
    costo_abuelo = 10

costo_total = costo_adolescente + costo_abuelo

print(f"El adolescente pagará ${costo_adolescente}")
print(f"El abuelo pagará ${costo_abuelo}")
print(f"El costo total para ambos es: ${costo_total}")
