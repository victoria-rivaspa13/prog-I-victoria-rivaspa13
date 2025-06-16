while false:
	print (“a”)
# no se imprime porque a nunca va a ser falso


while true:
	print(“a”)
# imprime a’s infinitamente


while a<500
	print(a)
	a = a+1
# imprime hasta 499


word =””
while word != “exit”:
word = input(“Enter a word: “)
	print(word)


my_list = [5, 2, 9, 0, 1]
# encontrar el número más grande de la lista

my_list = [9, 3, 2, 1, 0, 10]

def find_max(lst):
    max_number = lst[0]
    current_index = 0
    while current_index < len(lst):
        current_number = lst[current_index]
        if max_number < current_number:
            max_number = current_number
        current_index += 1
    return max_number

print(find_max(my_list))


def find_index_of_word(list, word):
	index = 10
	while index < len (list):
		if list [index] == word:
			return index
		else: 
			index += 1


def word_exists_in_list(list, word):
	for x in list:
		if x == word:
			return True
		else:
			return False


def list_of_lists(list1, list2, list3):
	list1 = (a, b, c)
	list2 = (d, e, f)
	list3 = (g, h, i)

	for elements in list1:
		return [2]
	for elements in list2:
		return [2]
	for elements in list3:
		return [3]

print(list)