from tkinter import *

window = Tk()
#labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=3)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=3)

#Entry
e1 = Entry(window)
e1.grid(row=0, column=1)

e2 = Entry(window)
e2.grid(row=0, column=3)

e3 = Entry(window)
e3.grid(row=1, column=1)

e4 = Entry(window)
e4.grid(row=1, column=3)

window.mainloop()