import tkinter as tk
from tkinter import *
import time

print("Python UI")
window = tk.Tk()
window.attributes('-fullscreen', False)
window.title("IOT Project")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print("Size:", screen_width, screen_height)


labelAMONIAValue = tk.Label(text="5.12",fg="#0000ff",justify=CENTER,font="Helvetica 60 bold")

labelAMONIAValue.place(x=0, y=200, width=screen_width / 3, height=100)
labelAMONIA = tk.Label(text="NH3",
                                fg="#0000ff",
                                justify=CENTER,
                                font="Helvetica 60 bold")
labelAMONIA.place(x=0, y=100, width=screen_width / 3, height=100)

labelTDSValue = tk.Label(text="20",
                                 fg="#0000ff",
                                 justify=CENTER,
                                 # bg = "#333",
                                 font="Helvetica 60 bold")

labelTDSValue.place(x=screen_width / 3, y=200, width=screen_width / 3, height=100)
labelTDS = tk.Label(text="TDS",
                                fg="#0000ff",
                                justify=CENTER,
                                font="Helvetica 60 bold")
labelTDS.place(x=screen_width / 3, y=100, width=screen_width / 3, height=100)


labelPHValue = tk.Label(text="7.11",
                                fg="#0000ff",
                                justify=CENTER,
                                font="Helvetica 60 bold")

labelPHValue.place(x=2 * screen_width / 3, y=200, width=screen_width / 3, height=100)

labelPH = tk.Label(text="PH",
                                fg="#0000ff",
                                justify=CENTER,
                                font="Helvetica 60 bold")

labelPH.place(x=2 * screen_width / 3, y=100, width=screen_width / 3, height=100)


buttonON= tk.Button(text="ON",fg="#0000AA",
                                justify=CENTER,
                                font="Helvetica 60 bold")

buttonON.place(x=0, y=400, width=screen_width / 3, height=100)

buttonOFF= tk.Button(text="OFF",fg="#0000AA",
                                justify=CENTER,
                                font="Helvetica 60 bold")
buttonOFF.place(x=screen_width / 2, y=400, width=screen_width / 3, height=100)


def nut_nhan_1():
    print("Bat")


def nut_nhan_2():
    print("Tat")

buttonON.config(command=nut_nhan_1)
buttonOFF.config(command=nut_nhan_2)