# I made this cause I wanna code in python again

# It's best to do this with 2 monitors, one for the game and one for the script

# Imports
import pyautogui as computer
import time
import keyboard
import sys
import PySimpleGUI as gui

# FUnctions

class cookies:
    def set():
        gui.popup("Setting cookies...")
        
    def add():
        gui.popup("Adding cookies...")
        time.sleep(3)
        computer.rightClick(3900, 723)
        computer.click(3954, 802)
        computer.click(4748, 80)
        computer.click(4600, 224)
        computer.typewrite("console.log('Added 1 cookie')")
class utils:
    def mousePos():
        while True:
            print(computer.position())
            if keyboard.is_pressed("q"):
                break
    def goto(x, y):
        computer.moveTo(x, y)

def start():
    window = gui.Window('🍪', [[gui.Text('Choose one of the below options')], [gui.Button('Set Cookies')], [gui.Button('Add Cookies'), gui.Button('Exit')]], margins=(300, 150))

    while True:
        event, values = window.read()
        if event == 'Set Cookies':
            cookies.set()
        elif event == 'Add Cookies':
            cookies.add()
        elif keyboard.is_pressed("space"):
            computer.click()
            time.sleep(0.1)
        elif keyboard.is_pressed("q"):
            gui.popup("🍪 == Exiting Program == 🍪")
            sys.exit()
        elif event == 'Exit':
            gui.popup("🍪 == Exiting Program == 🍪")
            sys.exit()

# Main
if __name__ == "__main__":
    start()	