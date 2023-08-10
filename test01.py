import pyautogui
import time
message = 1

while message < 10:
    time.sleep(1)
    pyautogui.typewrite('Uff maroof ' + str(message))
    # pyautogui.hotkey("alt", "127789")
    time.sleep(1)
    pyautogui.press('enter')
    message = message + 1
