from tkinter import *
from tkinter.ttk import * 
from tkinter import messagebox
from methods import *

app = Tk()  # Window config
app.iconbitmap("math.ico")
app.title("SetsCalc")
app.geometry("220x95")
app.resizable(0, 0)


def clear():
    first_set_entry.delete(0, END)
    second_set_entry.delete(0, END)


# main logic
def display():
    full_set = first_set_entry.get() + " " + second_set_entry.get()  # Union
    full_set = full_set.split(" ")
    full_set = list(map(int, full_set))
    full_set = unique(full_set)
    full_set.sort()
    in_order(full_set)

    first_set = first_set_entry.get()  # Intersection
    first_set = first_set.split(" ")
    first_set = list(map(int, first_set))
    second_set = second_set_entry.get()
    second_set = second_set.split(" ")
    second_set = list(map(int, second_set))
    intersection = set(first_set) & set(second_set)
    messagebox.showinfo("Intersec", intersection)

    a_minus_b = str(set(first_set) - set(second_set))  # Difference
    b_minus_a = str(set(second_set) - set(first_set))
    messagebox.showinfo("Difference", "A \\ B: " + a_minus_b + " " + "B \\ A: " + b_minus_a)

    difference = "{" + str(a_minus_b) + ',' + str(b_minus_a) + "}"  # Symmetric Difference
    messagebox.showinfo("Symmetric Difference", difference)


first_set_label = Label(text="First Set:")
second_set_label = Label(text="Second Set:")
first_set_label.grid(row=0, column=0, sticky="w")
second_set_label.grid(row=1, column=0, sticky="w")

first_set_entry = Entry()
second_set_entry = Entry()

first_set_entry.grid(row=0, column=1, padx=5, pady=5)
second_set_entry.grid(row=1, column=1, padx=5, pady=5)
first_set_entry.insert(0, "2 3 7 8")
second_set_entry.insert(0, "3 4 6 7 10 12 13 14 11")

display_button = Button(text="Display", command=display)
clear_button = Button(text="Clear", command=clear)
display_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

app.mainloop()
