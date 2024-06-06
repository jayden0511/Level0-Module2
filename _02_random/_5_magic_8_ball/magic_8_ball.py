import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring('title 20', 'are you smart')
    # Make a variable and initialize it to a random number between 0 and 3
    v=random.randint(0, 3)
    # If the random number is 0
    if v ==0:
        messagebox.showinfo('title 21', 'yes')
        # tell the user "Yes"

    # If the random number is 1
    elif v ==1:
        messagebox.showinfo('title 22', 'no')
        # tell the user "No"

    # If the random number is 2
    elif v ==2:
        messagebox.showinfo('title 23', 'maybe you should ask google')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    elif v ==3:
        messagebox.showinfo('title 24', 'no')
        # write your own answer
