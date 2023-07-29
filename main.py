import random
import tkinter as tk
import pyautogui

IMAGES_PATH: str = "./sprites/cat.gif"


def main() -> None:
    x: int = 1400
    cycle: int = 0
    check: bool = 1
    idle_num: list[int] = [1, 2, 3, 4]
    sleep_num: list[int] = [10, 11, 12, 13, 15]
    walk_left: list[int] = [6, 7]
    walk_right: list[int] = [8, 9]
    event_number: int = random.randrange(1, 3, 1)

    window: tk.Tk = tk.Tk()

    # call buddy's action .gif to an array
    cat = [
        tk.PhotoImage(file=IMAGES_PATH + "cat.gif", format="gif -index %i" % (i))
        for i in range(5)
    ]

    # configure window settings
    window.config(highlightbackground='black')
    window.overrideredirect(True)
    window.wm_attributes('-transparentcolor', 'black')

    label = tk.Label(window, bd=0, bg='black')
    label.pack()

    window.mainloop()



if __name__ == "__main__":
    main()
