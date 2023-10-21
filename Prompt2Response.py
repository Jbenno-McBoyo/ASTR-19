import numpy.random as random

flt1 = random.rand()
flt2 = random.rand()
int1 = random.randint(-20,21)

print(f'Sum of two floats: {flt1+flt2} is a {type(flt1+flt2)} value')
print(f'Difference of two floats: {flt1-flt2} is a {type(flt1-flt2)} value')
print(f'Product of a float and an int: {flt1*int1} is a {type(flt1*int1)} value')
