import pyautogui
import keyboard
import time

# config
timeHolding = 1.7
repeatProcess = 25
waitingTime = 0.3

print('Configurations:')
print('Time Holding: '+str(timeHolding))
print('Repeat Times: '+str(repeatProcess))
print('Delay: '+str(waitingTime))

print("________________________________")

isCustom = input("Change configurations? (yes / no)")
if isCustom == "yes":
    timeHolding = float(input("Time Holding:"))
    repeatProcess = int(input("Repeat Process:"))
    waitingTime = float(input("Delay:"))
    print('New Configurations:')
    print('Time Holding: ' + str(timeHolding))
    print('Repeat Times: ' + str(repeatProcess))
    print('Delay: ' + str(waitingTime))

print("________________________________")
time.sleep(1)

print('Press SHIFT to start')
print('Press CTRL to cancel')
print('Put cursor in the corner to stop while executing automation')

while True:
    if keyboard.is_pressed('shift'):
        print("________________________________")
        print('starting loop for ' + str(repeatProcess) + ' times')
        for i in range(repeatProcess):
            print('time: '+str(i+1)+'/'+str(repeatProcess))
            pyautogui.keyDown('w')
            pyautogui.mouseDown()
            time.sleep(timeHolding)
            pyautogui.keyUp('w')
            pyautogui.mouseUp()
            time.sleep(waitingTime)
        pyautogui.press('shift')
        print("________________________________")
        print('complete')
        print('Press CTRL to stop or SHIFT to restart')
    elif keyboard.is_pressed('ctrl'):
        print("________________________________")
        print('stopping...')
        time.sleep(1)
        exit(0)
