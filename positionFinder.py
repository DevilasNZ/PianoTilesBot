#use this program to find where the mouse is on the screen.

import time
import pyautogui

print("screen resolution: " + str(pyautogui.size()))

while True:#keep running this program until it is closed.
    print(pyautogui.position())
    time.sleep(1)
