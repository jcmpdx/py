import math

w = input('Enter weight in pounds: ')
print(f'{w}: is the weight you entered.')
w = float(w)
lbs = math.trunc(w)
oz = w - lbs
oz = 16 * oz
oz = round(oz,2)
print(f'{lbs}lbs. {oz}oz.')