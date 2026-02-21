n = int(input("Enter a positive integer:"))


if n <=0:
    print("Please enter a positive integer.")
else:
    #
    total = n * (8 + 1) // 2

    print("The sum of the first", n, "positive integers is:", total)
