import tkinter as tk

from sprites import Sprite
from typing import List
from sys import platform

class Window:
    root: tk.Tk
    sprites = List[Sprite]
    current_sprite_index: int
    label: tk.Label

    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root)
        self.current_sprite_index = 0

        self.sprites = list()

        self.root.config(highlightbackground='black')
        self.root.overrideredirect(True)
        if platform == "win32":
            self.root.wm_attributes('-transparentcolor','black')
        else:
            self.root.wait_visibility(self.root)
            self.root.attributes('-alpha', 0.9)

    def add_sprite(self, sprite: Sprite):
        self.sprites.append(sprite)


    def mainloop(self):
        self.label.pack()
        self.root.after(0, self.update, 0)
        self.root.mainloop()

    def set_current_sprite(self, index: int):
        if index < len(self.sprites):
            self.current_sprite_index = index


    def update(self, index: int):
        current_sprite: Sprite = self.sprites[self.current_sprite_index]
        frame = current_sprite.frames[index]

        index += 1
        if index == current_sprite.frame_count:
            index = 0

        self.root.geometry(current_sprite.get_geometry())
        self.label.configure(image=frame)
        
        current_sprite.update_sprite()
        self.root.after(100, self.update, index)

        

    
        
