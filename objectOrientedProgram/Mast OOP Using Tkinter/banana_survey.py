"""A banana preferences survey written in Python with Tkinter"""
from email import message
import tkinter as tk

# [TODO](Widgets and layout are mixed together,
# widgets put together, layouts put together is better)

root = tk.Tk()
root.title("Banana interest survey")
root.geometry('640x480+200+200')
root.resizable(False, False)

title = tk.Label(root, text="Please take the survey",
                 font=("Arial 16 bold"), bg="brown", fg="#FF0")
title.grid(columnspan=2)

name_var = tk.StringVar(root)
name_label = tk.Label(root, text="What is your name?")
name_inp = tk.Entry(root, textvariable=name_var)
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)

eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(root, variable=eater_var,
                           text="Check this box if you eat bananas")
eater_inp.grid(row=2, columnspan=2, sticky='we')


# Spinbox
num_var = tk.IntVar(value=3)
num_label = tk.Label(root, text="How many bonanas do you eat per day?")
num_inp = tk.Spinbox(root, textvariable=num_var, from_=0, to=1000, increment=1)
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))


# OptionMenu
# # Add choices
color_choices = (
    'Any', 'Green', 'Green-Yellow', "Yellow", "Brown Spotted", "Black"
)
color_var = tk.StringVar(value="Any")
color_label = tk.Label(root, text="What is the best color for a banana?")
color_inp = tk.OptionMenu(root, color_var, *color_choices)

color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)


# Radiobutton
plantain_label = tk.Label(root, text="Do you eat plantains?")
plantain_frame = tk.Frame(root)
plantain_var = tk.BooleanVar()
plantain_yes_inp = tk.Radiobutton(
    plantain_frame, text="Yes", value=True, variable=plantain_var)
plantain_no_inp = tk.Radiobutton(
    plantain_frame, text="Ewww, no!", value=False, variable=plantain_var)

plantain_yes_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
plantain_no_inp.pack(side="left", fill="x", ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)


# Text Widget
banana_haiku_label = tk.Label(root, text="Write a haiku about bananas")
banana_haiku_inp = tk.Text(root, height=3)
banana_haiku_label.grid(row=8, sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky="NSEW")


# Submit Button
submit_btn = tk.Button(root, text="Submit Survey")
submit_btn.grid(row=99)


# Output Lable
output_var = tk.StringVar(value='')
output_line = tk.Label(root, textvariable=output_var,
                       anchor='w', justify='left')
output_line.grid(row=100, columnspan=2, sticky="NSEW")


# Configure Submit Button
def on_submit():
    """To be run when the user submits the form"""
    try:
        number = num_inp.get()
    except tk.TclError:
        number = 1000
    # The contents of name_inp widget and variable name_var are kept in sync
    name = name_var.get()
    color = color_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()

    # Get text widget contents
    haiku = banana_haiku_inp.get("1.0", tk.END)

    message = f"Thanks for taking this survey, {name}.\n"
    if not banana_eater:
        message += "Sorry you don't like bananas!\n"
    else:
        message += f"Enjoy your {number} {color} bananas!\n"
    if plantain_eater:
        message += "Enjoy you plantains!"
    else:
        message += "May you successfully avoid plantains!"
    if haiku.strip():
        message += f"\n\n    Your Haiku:\n{haiku}"

    output_var.set(message)


submit_btn.configure(command=on_submit)

root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

root.mainloop()
