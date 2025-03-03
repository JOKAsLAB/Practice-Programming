# entrybox

from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username + "!")
    entry.config(state=DISABLED)
    
def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial",50),
              fg="green",
              bg="black",
              show="*")

# entry.insert(0, "Spongebob")
# entry.pack(side=LEFT)
# entry.config(state=DISABLED)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()