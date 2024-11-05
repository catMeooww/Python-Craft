import pyautogui
import keyboard
import time

# config
keyToWalk1 = "a"
keyToWalk2 = "s"
keyToWalk3 = "d"
blocksByRow = 20
blocksByCollum = 5
startHotbar = "1"
maxHotbar = "9"

print("__Configurations_________________________")
print("Keys:",keyToWalk1,keyToWalk2,keyToWalk3)
print("Total Blocks (row x collum):",blocksByRow," x ",blocksByCollum)
print("Hotbar:",startHotbar," - ",maxHotbar)

print("_________________________________________")

isCustom = input("Change Config (yes/no):")

if isCustom == "yes":
    keyToWalk1 = input("Key to walk 1 (w,a,s,d):")
    keyToWalk2 = input("Key to walk 2 (w,a,s,d):")
    keyToWalk3 = input("Key to walk 3 (w,a,s,d):")
    blocksByRow = int(input("Blocks by Row (number):"))
    blocksByCollum = int(input("Blocks by Collum (number):"))
    startHotbar = input("first slot (slotId):")
    maxHotbar = input("last slot (slotId):")

    print("__New_Configurations__________________")
    print("Keys:",keyToWalk1,keyToWalk2,keyToWalk3)
    print("Total Blocks (row x collum):",blocksByRow," x ",blocksByCollum)
    print("Hotbar:",startHotbar," - ",maxHotbar)

elif isCustom == "blocks":
    blocksByRow = int(input("Blocks by Row (number):"))
    blocksByCollum = int(input("Blocks by Collum (number):"))
    print("__New_Configurations__________________")
    print("Total Blocks (row x collum):",blocksByRow," x ",blocksByCollum)

elif isCustom == "keys":
    keyToWalk1 = input("Key to walk 1 (w,a,s,d):")
    keyToWalk2 = input("Key to walk 2 (w,a,s,d):")
    keyToWalk3 = input("Key to walk 3 (w,a,s,d):")
    print("__New_Configurations__________________")
    print("Keys:",keyToWalk1,keyToWalk2,keyToWalk3)

elif isCustom == "hotbar":
    startHotbar = input("first slot (slotId):")
    maxHotbar = input("last slot (slotId):")
    print("__New_Configurations__________________")
    print("Hotbar:",startHotbar," - ",maxHotbar)

totalBlocks = blocksByRow * blocksByCollum
placedBlocks = 0
selectedHotbar = startHotbar
lastChange = 64
nowKey = keyToWalk1

print("_________________________________________")
print("Total Blocks:",totalBlocks)
print("Packs:",totalBlocks / 64)
print("Warning: Shift in Toggle Mode required!")
print("_________________________________________")

time.sleep(1)

print('Press SHIFT to start')
print('Press CTRL to cancel')
print('Put cursor in the corner to stop while executing automation')

while True:
    if keyboard.is_pressed('shift'):
        print("________________________________")
        print('starting loop for place',totalBlocks,"blocks")
        pyautogui.press(selectedHotbar)
        for i in range(blocksByCollum):
            pyautogui.keyDown(keyToWalk2)
            time.sleep(0.7)
            pyautogui.keyUp(keyToWalk2)
            for b in range(blocksByRow):
                if placedBlocks == lastChange:
                    lastChange = lastChange + 64
                    if int(selectedHotbar) < int(maxHotbar):
                        selectedHotbar = str(int(selectedHotbar)+1)
                        pyautogui.press(selectedHotbar)
                    else:
                        print("________________________________")
                        print("Max Hotbar Reached")
                        decision = input("Type 0 to stop program or 1 to return to first slot:")
                        time.sleep(2)
                        if decision == "0":
                            pyautogui.press('shift')
                            exit(1)
                        else:
                            selectedHotbar = startHotbar
                            pyautogui.press(selectedHotbar)
                pyautogui.click(button='right')
                pyautogui.keyDown(nowKey)
                placedBlocks = placedBlocks + 1
                print("Placed:",placedBlocks,"/",totalBlocks)
                time.sleep(0.7)
                pyautogui.keyUp(nowKey)
            if nowKey == keyToWalk1:
                nowKey = keyToWalk3
            else:
                nowKey = keyToWalk1
            time.sleep(0.2)
            pyautogui.keyDown(nowKey)
            time.sleep(0.7)
            pyautogui.keyUp(nowKey)
            print("Collum:",i+1,"/",blocksByCollum)
        pyautogui.press('shift')
        print("________________________________")
        print('complete')
        print('Press CTRL to stop or SHIFT to restart')
    elif keyboard.is_pressed('ctrl'):
        print("________________________________")
        print('stopping...')
        time.sleep(1)
        exit(0)