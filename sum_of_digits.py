from functools import reduce

numbers = [1, 2, 3, 4]

sum_of_digits= reduce(lambda x,y: x+y, numbers)

print(sum_of_digits)