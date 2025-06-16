def collect_numbers():
    numbers = []
    number = int(input("Enter a positive number (or 0 to finish): "))

    while number != 0:
        if number > 0:
            numbers.append(number)
        else:
            print("Please enter a positive number.")
        number = int(input("Enter a positive number (or 0 to finish): "))
    reverse = numbers[::-1]
    print(reverse)

collect_numbers()

