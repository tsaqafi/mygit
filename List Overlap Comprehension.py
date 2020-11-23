# write a program that return a lsit that contains only the elements
# that are common between the lists(without duplicate)
# Two list of different sizes
# import random

# a = random.sample(range(100), 5)
# b = random.sample(range(100), 4)
x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_overlap = [b for a in x for b in y if a == b]

print(list_overlap)
