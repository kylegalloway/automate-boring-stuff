import pyautogui

pyautogui.click(100, 100)  # For correct focus
pyautogui.typewrite('Hello world', interval=0.2)  # String to write
# Strings and other buttons (left, ctrl, f1, etc.)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.2)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.press('f1')  # single key
pyautogui.hotkey('ctrl', 'o')  # press at the same time
