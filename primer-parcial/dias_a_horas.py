def dias_a_horas(dias):
    if dias >= 0:
        horas = dias * 24
        return horas
    else:
        return "Número erróneo de dias ingresados"

horas_1 = dias_a_horas(5)
horas_2 = dias_a_horas(0)
horas_3 = dias_a_horas(-4)

print(f"{horas_1} horas")
print(f"{horas_2} horas")
print(f"{horas_3} horas")