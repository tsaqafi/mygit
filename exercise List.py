# List less than ten
# list number elements if conditional

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

for i in a:
    if i < 5:  # Conditional statement if number is less than 5 is printed
        x.append(i)
        print(x)

