import re
import pyperclip as pc
from tkinter import messagebox

text = pc.paste()
output = re.sub('\s+','\', \'',text)

o2 = "'{}'".format(output)
pc.copy(o2)
messagebox.showinfo('Done!','Results in your clipboard. paste in a text document to view results')

# This py file takes text on multiple rows/lines, and puts them all on 1 line. It also wraps each string in single-quotes, and puts a comma between them. 
# Useful when you need to convert a list of items into a string you can filter on.

# Example - it'll convert the following...

# Banana
# Ham
# Cheese

# ...into...

# 'Banana', 'Ham', 'Cheese'

# HOW TO USE
# 1. Copy the text into your clipboard (select the text + CONTROL C)
# 2. Run the py file
# 3. Paste into a text document
