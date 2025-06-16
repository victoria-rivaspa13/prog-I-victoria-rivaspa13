a = 9
b = False
if a > 1 and a < 9:
	a = 3
	b = True
elif a < 0 or a > 8:
	if a == 9:
		a = 5
		b = True
	else:
		a = 20
		b = False
	if b:
		a = 3
	else:
		a = 8

print(a)
print(b)