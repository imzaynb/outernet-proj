import functools
from commands import type_words_into_tab, win_closing
from thread import RunCommandsAsync
from window import Window
from sprites import Sprite
from initial_gui import QtFrontWindow
import sys
from PyQt6.QtWidgets import QApplication
from text import ms_paint

def main():
    # Run the other Python file using subprocess
    # Now continue with the rest of the code
    def submitButtonCommand():
        win_closing() 
        window: Window = Window()
        cat: Sprite = Sprite("./sprites/turtle_med.gif", 100, 100, 5, 0, 0, 1, 1, 50, 50)
        window.add_sprite(cat)

        commands = [
            functools.partial(type_words_into_tab, "google.com", "HEHEHE I AM IN CONTROL NOW"),
            functools.partial(type_words_into_tab, "google.com", "WHAT ARE YOU WAITING FOR? TRY TO KILL ME:)"),
            functools.partial(type_words_into_tab, "google.com", "MEANWHILE IMMA HAVE SOME FUN:))"),
            functools.partial(cat.set_offset_x,0),
            functools.partial(cat.set_offset_y,0),
            functools.partial(ms_paint),
            functools.partial(cat.set_offset_x,50),
            functools.partial(cat.set_offset_y,50)
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
