import functools
import time
from commands import move_mouse_randomly, type_words_into_tab, win_closing, rick_roll, move_mouse_to_location
from thread import RunCommandsAsync
from window import Window
from sprites import Sprite
from initial_gui import QtFrontWindow
import sys
from PyQt6.QtWidgets import QApplication
from text import ms_paint
from blockinput import block_keyboard, block_mouse, enable_keyboard, enable_mouse
import os

HAPPY_TURTLE_INDEX: int = 0
TAUNTING_TURTLE_INDEX: int = 1
SUPER_SAIYAN_TURTLE_INDEX: int = 2
KNIFE_TURTLE_INDEX: int = 3

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    # Run the other Python file using subprocess
    # Now continue with the rest of the code
    def submitButtonCommand():
        win_closing() 
        window: Window = Window()

        happy_turtle: Sprite = Sprite(os.path.join(ROOT_DIR, "sprites\\happy-turtle_med.gif"), 100, 100, 22, 0, 0, 1, 1, 50, 50)
        taunting_turtle: Sprite = Sprite(os.path.join(ROOT_DIR, "sprites\\laughing-turtle_med.gif"), 100, 100, 17, 0, 0, 1, 1, 50, 50)
        super_saiyan_turtle: Sprite = Sprite(os.path.join(ROOT_DIR, "sprites\\super-saiyan-turtle_med.gif"), 100, 100, 21, 0, 0, 1, 1, 50, 50)
        knife_turtle: Sprite = Sprite(os.path.join(ROOT_DIR, "sprites\\turtle_med.gif"), 100, 100, 4, 0, 0, 1, 1, 50, 50)

        window.add_sprite(happy_turtle)
        window.add_sprite(taunting_turtle)
        window.add_sprite(super_saiyan_turtle)
        window.add_sprite(knife_turtle)

        commands = [
            functools.partial(block_mouse),
            functools.partial(move_mouse_to_location, 500, 500),
            functools.partial(window.set_current_sprite, SUPER_SAIYAN_TURTLE_INDEX),
            functools.partial(time.sleep, 3),
            functools.partial(type_words_into_tab, "google.com", "HEHEHE I AM IN CONTROL NOW"),
            functools.partial(type_words_into_tab, "google.com", "WHAT ARE YOU WAITING FOR? TRY TO KILL ME:)"),
            functools.partial(type_words_into_tab, "google.com", "MEANWHILE IMMA HAVE SOME FUN:))"),
            functools.partial(super_saiyan_turtle.set_offset_x,0),
            functools.partial(super_saiyan_turtle.set_offset_y,0),
            functools.partial(enable_mouse),
            functools.partial(ms_paint),
            functools.partial(block_mouse),
            functools.partial(super_saiyan_turtle.set_offset_x,50),
            functools.partial(super_saiyan_turtle.set_offset_y,50),
            functools.partial(move_mouse_to_location, 500, 500),
            functools.partial(window.set_current_sprite, TAUNTING_TURTLE_INDEX),
            functools.partial(time.sleep, 3),
            functools.partial(enable_mouse),
            functools.partial(rick_roll),
            functools.partial(move_mouse_randomly),
            functools.partial(move_mouse_randomly),
            functools.partial(move_mouse_randomly),
            functools.partial(move_mouse_randomly),
            functools.partial(move_mouse_randomly),
            functools.partial(move_mouse_randomly),
            functools.partial(move_mouse_randomly),
        ]

        thread = RunCommandsAsync(window.root, commands)

        window.mainloop()
    
    app = QApplication(sys.argv)

    window = QtFrontWindow()
    window.setButtonCommand(submitButtonCommand)
    window.show()
    sys.exit(app.exec())




if __name__ == "__main__":
    main()
