import subprocess as sb_p
import tkinter as tk
from tkinter import *


def Home(root, frame1, frame2):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    Label(frame2, text="                                                                         ").grid(row = 0,column = 1)
    Label(frame2, text="                                                                         ").grid(row = 0,column = 2)
    Label(frame2, text="         ").grid(row = 1,column = 1)
    frame2.pack(side=TOP)

    root.title("Home")


    newTab = Button(frame1, text="Run Camera", width=15, command = lambda: sb_p.call('python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel', shell=True))


    newTab.grid(row = 7, column = 2, columnspan = 2)
    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('350x350')
    frame1 = Frame(root)
    frame2 = Frame(root)
    Home(root, frame1, frame2)


if __name__ == "__main__":
    new_home()