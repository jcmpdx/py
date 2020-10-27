import pyautogui
print(pyautogui.size())
print(pyautogui.position())
# PyAutoGUI has a auto-quit if you position the mouse cursor in at 0,0
# moving the mouse to absolute position
pyautogui.moveTo(10,10, duration=2)

# move relative to where mouse cursor currently is located
pyautogui.moveRel(0, 200, duration=1)
pyautogui.click(300, 38)
# pyautogui.doubleClick(x, y)
# pyautogui.dragTo/dragRel

# pyautogui has a mini-program in the command prompt that can show you real time mouse cursor and RGB value of the pixel you're hovered over