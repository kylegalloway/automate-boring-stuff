import pyautogui

pyautogui.screenshot('/mnt/c/Users/ckgallow/Downloads/screenshot_example.png')
# find x,y,width,height of partial image on screen
pyautogui.locateOnScreen('calc7key.png')
# find x,y center of partial image on screen
center_x, center_y = pyautogui.locateCenterOnScreen('calc7key.png')

pyautogui.click(center_x, center_y)
