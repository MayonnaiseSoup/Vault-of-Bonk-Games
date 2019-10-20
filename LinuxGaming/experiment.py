from tkinter import (Tk, Button)

def bAaction():
    import caterpillargame

def bBaction():
    import pacman

def bCaction():
    import connect

def bDaction():
    import Matchmaker

def bEaction():
    import NineLives

root = Tk()
buttonA = Button(root, text="Caterpillar Game", command=bAaction)
buttonB = Button(root, text="Pacman", command=bBaction)
buttonC = Button(root, text="Connect 4", command=bCaction)
buttonD = Button(root, text="Match Maker", command=bDaction)
buttonE = Button(root, text="Nine Lives (Terminal Game)", command=bEaction)

buttonE.pack()
buttonA.pack()
buttonB.pack()
buttonC.pack()
buttonD.pack()
root.mainloop()
