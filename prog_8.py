def is_prime(number):
    if number < 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
                break
        return True


num = int(input("Enter a Number to check Prime: "))
print(is_prime(num))
