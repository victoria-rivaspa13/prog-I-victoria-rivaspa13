def longest (a, b):
    global todo
    todo = a + b
    if len(a) > len(b):
        return a
    else:
        return b

logest("ahora", "recreo")