# Created by Jordan Leich on 8/10/2020


# Imports
import time
from tkinter import *
import os

window = Tk()
window.title("Power Options")

w = 370
h = 135

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.wm_attributes("-alpha", 0.80)

filename = PhotoImage(file="images\image.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def shutdown():
    time.sleep(.500)
    shutting_down = Label(window, text="Shutting down your computer...", fg='black', bg='red')
    shutting_down.grid(row=3, column=0, padx=5, pady=5)
    os.system("shutdown /s /t 5")


def hibernate():
    time.sleep(.500)
    sleeping_label = Label(window, text="Hibernating your computer...", fg='black', bg='purple')
    sleeping_label.grid(row=3, column=0, padx=5, pady=5)
    os.system("shutdown /h")


def restart():
    time.sleep(.500)
    restarting_label = Label(window, text="Restarting your computer...", fg='black', bg='orange')
    restarting_label.grid(row=3, column=0, padx=5, pady=5)
    os.system("shutdown /r /t 3")


def log_off():
    time.sleep(.500)
    log_label = Label(window, text="Logging off your computer...", fg='black', bg='yellow')
    log_label.grid(row=3, column=0, padx=5, pady=5)
    time.sleep(1.5)
    os.system("shutdown /l")


def closing():
    window.destroy()
    exit()


def start():
    shutdown_button = Button(window, text="Shutdown Computer", command=shutdown, fg='black', bg='red')
    shutdown_button.grid(row=0, column=0)

    sleep_button = Button(window, text="Hibernate Computer", command=hibernate, fg='black', bg='purple')
    sleep_button.grid(row=0, column=1, padx=5, pady=5)

    restart_button = Button(window, text="Restart Computer", command=restart, fg='black', bg='orange')
    restart_button.grid(row=0, column=2, padx=5, pady=5)

    log_button = Button(window, text="Log Off", command=log_off, fg='black', bg='yellow')
    log_button.grid(row=1, column=0, padx=10, pady=5)

    exit_button = Button(window, text="Exit Program", command=closing, fg='black', bg='green')
    exit_button.grid(row=1, column=1, padx=5, pady=5)


start()
window.mainloop()
