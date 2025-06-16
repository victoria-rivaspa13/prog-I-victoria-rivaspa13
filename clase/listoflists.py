def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify) != 3:
        return False
    
    lista_modificada = []

    if len(list_of_lists_to_modify[0]) >= 2:
        lista_modificada.append(list_of_lists_to_modify[0][:2])
    else:
        lista_modificada.append(list_of_lists_to_modify[0])

    if len(list_of_lists_to_modify[1]) >= 4:
        lista_modificada.append(list_of_lists_to_modify[1][1:4])
    else:
        lista_modificada.append(list_of_lists_to_modify[1])

    if len(list_of_lists_to_modify[2]) >= 2:
        lista_modificada.append(list_of_lists_to_modify[2][-2:])
    else:
        lista_modificada.append(list_of_lists_to_modify[2])

    return lista_modificada

list_of_lists_to_modify = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print(list_of_lists(list_of_lists_to_modify))
