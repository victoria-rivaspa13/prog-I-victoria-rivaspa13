def compararStrings(str1, str2):
    if str1 == str2:
        return "exactamente iguales"
    elif str1.lower() == str2.lower():
        return "parecidos"
    else:
        return "distintos"

print(compararStrings("hola", "hola"))