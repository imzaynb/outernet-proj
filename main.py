from window import Window
from sprites import Sprite

def main():
    window: Window = Window()
    cat: Sprite = Sprite("./sprites/cat.gif", "100x100", 5, 0, 0, 1, 1)
    window.add_sprite(cat)
    window.mainloop()

if __name__ == "__main__":
    main()