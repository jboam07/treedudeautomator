import pyautogui
import time
pyautogui.FAILSAFE = True
side="left"

choice = input("Begin?")
if choice == "y":
    #lets you alt tab into the game
    time.sleep(4)
    while True:
        px = pyautogui.pixel(1215, 687)
        if px == (255, 255, 255):
            for i in range(2):
                pyautogui.hotkey('left')
                time.sleep(0.047)
        else:
            pyautogui.hotkey('right')
            time.sleep(0.047)
else:
    print("Cancelling...")
