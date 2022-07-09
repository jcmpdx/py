import math
import tkinter.messagebox

w = input('Enter weight in pounds: ')
print(f'{w}: is the weight you entered.')
w = float(w)
lbs = math.trunc(w)
oz = w - lbs
oz = 16 * oz
oz = round(oz,2)
spam = f'{lbs}lbs. {oz}oz. is the result of {w}lbs.'
tkinter.messagebox.showinfo('Results',spam)