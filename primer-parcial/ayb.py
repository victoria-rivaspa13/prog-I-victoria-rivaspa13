a = True
b = 9
if not a or b > 4:
	a = False
	b = b - 3
	if b > 6:
		a = True
	else:
		b= -b
else:
	b=b*2
b = b + 1

print(a)
print(b)