import pyautogui

print(pyautogui.size())

width, height = pyautogui.size()

print(pyautogui.position())  # mouse position

pyautogui.moveTo(10, 10)  # move mouse to 10,10
pyautogui.moveTo(10, 10, duration=1.5)  # move mouse to 10,10 slowly
pyautogui.moveRel(75, 0, duration=1.0)  # move relative to current position
pyautogui.click(339, 38)  # click with mouse at position
pyautogui.doubleClick(339, 38)  # double click with mouse at position
pyautogui.rightClick(339, 38)  # right click with mouse at position
pyautogui.middleClick(339, 38)  # middle click with mouse at position
