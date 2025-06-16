def slice_simple():
    texto = "Awesome"
    texto = texto.lower()
    primeras_tres = texto[:3]
    medio = texto[2:5]
    primera_cuarta = texto[:4]
    antepenultima_ultima = texto[-3:]
    ultimo = primera_cuarta + antepenultima_ultima
    print (primeras_tres)
    print(medio)
    print(ultimo)
slice_simple()