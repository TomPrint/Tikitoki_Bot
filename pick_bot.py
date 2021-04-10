import pyautogui
import time
import randomizer

#inspect #flexmode #Iphone6/7/8 not plus

for i in range(3):
    pyautogui.click(944, 561)
    time.sleep(3)

    pyautogui.click(1154, 664)  # open comment section
    time.sleep(3)

    pyautogui.click(805, 959)  # activate comment box
    time.sleep(5)

    pyautogui.write(randomizer.randomizing(), interval=0.3)  # write msg
    time.sleep(10)

    pyautogui.click(1158, 958)  # send
    time.sleep(3)

    pyautogui.click(914, 312)  # closing window
    time.sleep(4)

    pyautogui.moveTo(798, 728)
    pyautogui.dragTo(796, 196, 1.3)

# currentMouseX, currentMouseY = pyautogui.position()

# print(str(currentMouseX)+","+str(currentMouseY))

