# I made this cause I wanna code in python again

# It's best to do this with 2 monitors, one for the game and one for the script

# Imports
import pyautogui as computer
import time
import keyboard
import sys
import customtkinter
import pymongo
from pymongo import MongoClient
import os
import dotenv
from dotenv import load_dotenv

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x300")
root.title("🍪 Cookie Clicker Hack 🍪")

# Lists

lusername = []
lpassword = []


# Init


username = None
password = None


# Functions

class cookies:
    def set():
        gui.popup("Setting cookies...") #Replace with tkinter
        
    def add(amount):
        gui.popup("Adding cookies...") #Replace with tkinter
        time.sleep(3)
        computer.rightClick(3900, 723)
        computer.click(3954, 802)
        time.sleep(1)
        computer.click(4742, 112)
        
        computer.typewrite("Game.cookies += " + str(amount))
        computer.press("enter")
class functions:
    class utils:
        def mousePos():
            while True:
                print(computer.position())
                if keyboard.is_pressed("q"):
                    break
        def goto(x, y):
            time.sleep(2)
            computer.moveTo(x, y)
        def getInputValue(inpfield, list):
            list.clear()
            user_input = inpfield.get()
            list.append(user_input)
            #print("Added " + user_input + " to list" + str(list))
    class login():
        
        def login(username, password, label):

            label = label

            label.configure(text="Logging in...")
            label.update()
            
            label.configure(text="Getting variables...")
            label.update()
            time.sleep(0.5)

            functions.utils.getInputValue(username, lusername)
            functions.utils.getInputValue(password, lpassword)
            label.configure(text="Finished getting variables...")
            label.update()
            time.sleep(0.5)
            username = ''.join(lusername[0])
            password = ''.join(lpassword[0])
            label.configure(text="Username: " + username + "       Password: " + "********** (Hidden)")
            label.update()
            time.sleep(0.5)
            label.configure(text="Logging in...")
            label.update()
            time.sleep(0.5)
            
            load_dotenv()
            connectionstring = os.getenv('MONGODB')
            client = MongoClient(connectionstring)
            dbname = "cookiehacks"
            collection = "credentials"
            
            label.configure(text="Connected to database!")
            label.update()
            time.sleep(0.5)
            label.configure(text="Checking if credentials exist...")
            label.update()
            time.sleep(0.5)
            if client[dbname][collection].find_one({"username": username, "password": password}):
                label.configure(text="Cleaning up... estimated time: 0.2 seconds")
                label.update()
                time.sleep(0.2)
                username = []
                password = []
                label.configure(text="Opening main menu...")
                label.update()
                
            else:
                # State that the credentials are wrong
                label.configure(text="Wrong credentials!")
            
                time.sleep(2)
                label.configure(text="Cleaning up... estimated time: 0.2 seconds")
                username = []
                password = []
                time.sleep(0.1)
                label.configure(text="Cleaned")
                #Clear terminal
                #os.system("cls")
                


        def gui():
            frame = customtkinter.CTkFrame(master=root)
            frame.pack(pady=20, padx=60, fill="both", expand=True)

            label = customtkinter.CTkLabel(master=frame, text="Login")
            label.pack(pady=10, padx=10)

            username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
            username.pack(pady=10, padx=10)

            password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
            password.pack(pady=10, padx=10)

            

            login = customtkinter.CTkButton(master=frame, text="Login", command=lambda: functions.login.login(username, password, info))
            login.pack(pady=10, padx=10)

            info = customtkinter.CTkLabel(master=frame, text="Info")
            info.pack( pady=10, padx=10)


            root.mainloop()
            

            
            
            

class hack:
    def run():
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        window = customtkinter.CTkLabel(master=frame, text="🍪 Cookie Clicker Hack 🍪")
        window.pack(pady=12, padx=10)

        amount = customtkinter.CTkEntry(master=frame, placeholder_text="Amount")
        addbutton = customtkinter.CTkButton(master=frame, text="Add cookies", command=lambda: cookies.add(amount.get()))
        setbutton = customtkinter.CTkButton(master=frame, text="Set cookies", command=cookies.set)
        mousepos = customtkinter.CTkButton(master=frame, text="Mouse position", command=functions.utils.mousePos)
        goto = customtkinter.CTkButton(master=frame, text="Go to", command=functions.utils.goto)

        amount.pack(pady=10, padx=10)
        addbutton.pack(pady=10, padx=10)
        setbutton.pack(pady=10, padx=10)
        mousepos.pack(pady=10, padx=10)
        goto.pack(pady=10, padx=10)
        
        root.mainloop()

        #window = gui.Window('🍪', [[gui.Text('Choose one of the below options')], [gui.Input('')] ,[gui.Button('Set Cookies')], [gui.Button('Add Cookies'), gui.Button('Exit')]], margins=(300, 150))

        #while True:

        #    event, values = window.read()
        #    input = values[0]
        #    if event == 'Set Cookies':
        #        cookies.set()
        #    elif event == 'Add Cookies':
        #        cookies.add(input)
        #    elif keyboard.is_pressed("space"):
        #        computer.click()
        #        time.sleep(0.1)
        #    elif keyboard.is_pressed("q"):
        #        gui.popup("🍪 == Exiting Program == 🍪")
        #        sys.exit()
        #    elif event == 'Exit':
        #        gui.popup("🍪 == Exiting Program == 🍪")
        #        sys.exit()
    
# Main
if __name__ == "__main__":
    functions.login.gui()