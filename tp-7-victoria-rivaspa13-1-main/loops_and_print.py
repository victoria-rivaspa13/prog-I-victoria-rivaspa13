def enumerate_list(colors):
    enumerated_list = []
    counter = 0
    for index, item in enumerate(colors):
        if item:
            enumerated_list.append(f'{counter}. {item}')
            counter +=1
    return enumerated_list

def enumerate_backwards(colors):
    enumerated_list = []
    counter = 0
    for item in colors:
        if item:
            reversed_item = item[::-1]
            enumerated_list.append(f'{counter}. {reversed_item}')
            counter += 1
    return enumerated_list
