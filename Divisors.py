# Create a program that asks the user a number and then
# prints a list of all the divisor of that number.

x = int(input(print("What number do you choose: ")))
#x_int = int(x_str)
divisor = []
a = range(1, 100)

for i in a:
    div = x % i
    if div >= 1:
        print(div)
        # divisor.append(div)

# print("The Divisor of the number are ", divisor)
