from window import Window
from sprites import Sprite
import subprocess

def main():
    # Run the other Python file using subprocess
    subprocess.run(["python", "window-messing.py"])
    subprocess.run(["python", "window-closing.py"])
    # Now continue with the rest of the code
    window: Window = Window()
    cat: Sprite = Sprite("./sprites/cat.gif", "100x100", 5, 0, 0, 1, 1)
    print("hmmm")
    window.add_sprite(cat)
    window.mainloop()

if __name__ == "__main__":
    main()
