def esMayorDeEdad(año_nacimiento, mes_nacimiento, dia_nacimiento):
    dia_actual = 12
    mes_actual = 5
    año_actual = 2023
    edad = año_actual - año_nacimiento
    if mes_actual < mes_nacimiento or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
        edad -= 1
        return edad >= 18
    else:
        return False

print(esMayorDeEdad(1960, 8, 24))
