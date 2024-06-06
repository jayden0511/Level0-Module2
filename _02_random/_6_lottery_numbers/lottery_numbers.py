import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    b=random.randint(1, 100)
    c=random.randint(1, 100)
    d=random.randint(1, 100)
    e=random.randint(1, 100)
    f=random.randint(1, 100)
    g=random.randint(1, 100)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo("title", str(b) + ' ' + str(c) + ' ' + str(d) + ' '+ str(e) + ' ' + str(f) + ' ' + str(g))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
