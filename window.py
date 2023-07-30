import tkinter as tk

from sprites import Sprite

class Window:
    root: tk.Tk
    sprites = list[Sprite]
    current_sprite_index: int
    label: tk.Label

    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root)
        self.current_sprite_index = 0

        self.sprites = list()

        self.root.config(highlightbackground='black')
        self.root.overrideredirect(True)
        self.root.wm_attributes('-transparentcolor','black')
        self.root.attributes('-topmost', True)
        self.root.config(cursor="none")

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
        
        current_sprite.update_sprite_to_mouse()
        self.root.after(50, self.update, index)

        

    
        
