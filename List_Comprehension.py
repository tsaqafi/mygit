# Makes a new list that has only even elements
# in the lst

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a_even = []

for i in a:
    if i % 2 == 0:
        a_even.append(i)
print("The even element from the list are", a_even)