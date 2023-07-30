import tkinter as tk
import pyautogui


class Sprite:
    frames: list[tk.PhotoImage]
    frame_count: int

    image_path: str

    image_width: int
    image_height: int

    x: int
    y: int

    vx: int
    vy: int

    def __init__(self, image_path: str, image_width: int, image_height: int, frame_count: int, x: int, y: int, vx: int, vy: int):
        self.frame_count = frame_count
        self.image_path = image_path           
        self.frames = [tk.PhotoImage(file=image_path, format = 'gif -index %i' %(i)) for i in range(frame_count)]
        
        self.image_width = image_width
        self.image_height = image_height 
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update_sprite_constant(self):
        self.x += self.vx
        self.y += self.vy
    
    def update_sprite_to_mouse(self):
        mouse_position = pyautogui.position()
        self.x = int(mouse_position.x - self.image_width/2)
        self.y = int(mouse_position.y - self.image_height/2)

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


    @property
    def image_resolution(self):
        return f'{self.image_width}x{self.image_height}'
