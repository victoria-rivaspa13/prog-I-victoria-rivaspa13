def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
    else:
        return False

list_to_compare1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
list_to_compare2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']

print(check_lists(list_to_compare1,list_to_compare2))