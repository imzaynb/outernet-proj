from window import Window
from sprites import Sprite
from threading import Thread
import random
import tkinter as tk

def make_window(root):
    window: Window = Window(root)
    cat: Sprite = Sprite("./sprites/cat.gif", "100x100", 5, x=random.randint(0,983), y=random.randint(0,983), vx=random.randint(-2,2), vy=random.randint(-2,2))
    window.add_sprite(cat)
    window.mainloop()

def main():
    root = tk.Tk()
    for x in range(30):
        make_window(root)
    root.mainloop()
if __name__ == "__main__":
    main()