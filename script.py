from tkinter import *

window = Tk()
#labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

#Entry fields
e1 = Entry(window)
e1.grid(row=0, column=1)

e2 = Entry(window)
e2.grid(row=0, column=3)

e3 = Entry(window)
e3.grid(row=1, column=1)

e4 = Entry(window)
e4.grid(row=1, column=3)

#buttons
b1 = Button(window, text="View all")
b1.grid(row=2, column=6)

#Scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2 ,sticky='ns' )

#Display field
display = Listbox(window, height=10, width=25)
display.grid(row=2, column=1)

# Attach scrollbar
display.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=display.yview)

for i in range(100):
    display.insert(END, i)


window.mainloop()