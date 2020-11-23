# Ask the user for a number and determine
# Whether the number is prime or not

def check_prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                print(i, "times", num / i, "is", num)
                break
            else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

User_int = int(input(print("Key in a number")))
check_prime(User_int)
