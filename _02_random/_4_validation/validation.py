import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        random_number = random.randint(1, 5)
        print(random_number)
        if random_number ==1:
            messagebox.showinfo('title 15', "you are very nice")
        elif random_number==2:
            messagebox.showinfo('title 16', "you are very cool")
        elif random_number==3:
            messagebox.showinfo('title 17', "you are good at the game")
        elif random_number==4:
            messagebox.showinfo('title 18', "you care for others")
        elif random_number==5:
            messagebox.showinfo('title19', "you have a great personality")
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
