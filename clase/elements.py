def add_elements(list_to_add_elements):
    list_to_add_elements = ['Red', 'Green', 'White', 'Black']
    lista = list_to_add_elements
    lista.insert(0, 'Pink')
    lista.append('Yellow')
    return(lista)
result_list = add_elements([])
print(result_list)