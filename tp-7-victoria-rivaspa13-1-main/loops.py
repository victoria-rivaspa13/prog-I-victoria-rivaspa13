def index_of_by_index(word, lst, index):
    if index >= len(lst):  # Check if the index is out of range
        return -1
    for i in range(index, len(lst)):
        if lst[i] == word:
            return i
    return -1

def index_of_empty(list):
    for i, item in enumerate(list):
        if item == "":
            return i
    return -1

def index_of(word, list):
    for i, item in enumerate(list):
        if item == word:
            return i
    return -1


def put(word, list):
    for i, item in enumerate(list):
        if item == "":
            list[i] = word
            return i
    return -1

def remove(word, list):
    count = 0
    for i, item in enumerate(list):
        if item == word:
            list[i] = ""
            count += 1
    return count
