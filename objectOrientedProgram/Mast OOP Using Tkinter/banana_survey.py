"""A banana preferences survey written in Python with Tkinter"""
import tkinter as tk

root = tk.Tk()
root.title("Banana interest survey")
root.geometry('640x480+300+300')
root.resizable(False, False)

title = tk.Label(root, text="Please take the survey",
                 font=("Arial 16 bold"), bg="brown", fg="#FF0")
title.pack()

name_label = tk.Label(root, text="What is your name?")
name_inp = tk.Entry(root)

root.mainloop()
