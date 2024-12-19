num = int(input("Enter a number:\n"))
is_prime = True


if num <= 1:
    is_prime = False
else:
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print(is_prime)
