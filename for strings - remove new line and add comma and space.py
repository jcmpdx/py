import re
import pyperclip as pc
from tkinter import messagebox

text = pc.paste()
output = re.sub('\s+','\', \'',text)

o2 = "'{}'".format(output)
pc.copy(o2)
messagebox.showinfo('Done!','Results in your clipboard. paste in a text document to view results')