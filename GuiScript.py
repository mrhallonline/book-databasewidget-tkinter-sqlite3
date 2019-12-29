from tkinter import *

window = Tk()
window.geometry("500x300")

def view_all():
    pass

def search_entry():
    pass

def add_entry():
    pass

def update_selected():
    pass

def delete_selected():
    pass

def close():
    pass

#labels
l1 = Label(window, text="Title", width=10).grid(row=0, column=0)
l2 = Label(window, text="Author" , width=10).grid(row=0, column=2)
l3 = Label(window, text="Year", width=10).grid(row=1, column=0)
l4 = Label(window, text="ISBN", width=10).grid(row=1, column=2)

#Entry fields
e1 = Entry(window, width=25).grid(row=0, column=1)
e2 = Entry(window, width=25).grid(row=0, column=3)
e3 = Entry(window, width=25).grid(row=1, column=1)
e4 = Entry(window, width=25).grid(row=1, column=3)

#buttons
b1 = Button(window, text="View all", command=view_all, width=15).place(x=325, y=75)
b2 = Button(window, text="Search Entry", command=search_entry, width=15).place(x=325, y=100)
b3 = Button(window, text="Add Entry", command=add_entry, width=15).place(x=325, y=125)
b4 = Button(window, text="Update Selected", command=update_selected, width=15).place(x=325, y=150)
b5 = Button(window, text="Delete Selected", command=delete_selected, width=15).place(x=325, y=175)
b6 = Button(window, text="Close", command=close, width=15).place(x=325, y=200)

#Scrollbar
scrollbar = Scrollbar(window)
scrollbar.place(x=260, y=125 )

#Display field
display = Listbox(window, height=10, width=40)
display.place(x=15, y=75)

# Attach scrollbar
display.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=display.yview)

for i in range(100):
    display.insert(END, i)

window.mainloop()