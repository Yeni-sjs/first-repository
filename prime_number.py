def is_prime_number(x):
    if x <= 1:
        print("Error : ERRORERRORERRORERRORERRORERROR")
    else:
        for num in range(2,x):
            if x % num == 0:
                print("The number {num1} is a prime number.".format(num1=x))
    print("The number {num1} is a prime number.".format(num1=x))
