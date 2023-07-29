import tkinter as tk
from typing import List

class Sprite:
    frames: List[tk.PhotoImage]
    frame_count: int

    image_path: str
    image_resolution: str

    x: int
    y: int

    vx: int
    vy: int

    def __init__(self, image_path: str, image_resolution: str, frame_count: int, x: int, y: int, vx: int, vy: int):
        self.frame_count = frame_count
        self.image_path = image_path           
        self.frames = [tk.PhotoImage(file=image_path, format = 'gif -index %i' %(i)) for i in range(frame_count)]
        self.image_resolution = image_resolution
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update_sprite(self):
        self.x += self.vx
        self.y += self.vy

    def get_geometry(self):
        return f'{self.image_resolution}+{self.x}+{self.y}'
    
    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def set_vx(self, vx: int):
        self.vx = vx

    def set_vy(self, vy: int):
        self.vy = vy


