def index_of_by_index(word, lst, index):
    i = 0
    while i < len(word):
        current_index = word[i]
        if current_index == index:
            return i
        i += 1
    return -1
colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(index_of_by_index("Black", colors, 1))