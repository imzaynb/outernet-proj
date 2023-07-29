import tkinter as tk

IMAGE_PATH: str = "./sprites/"
root = tk.Tk()

FRAME_CNT: int = 5
frames = [tk.PhotoImage(file=IMAGE_PATH+"cat.gif", format = 'gif -index %i' %(i)) for i in range(FRAME_CNT)]

location: int = 0

def update(index: int) -> None:
    global location
    location += 1
    frame = frames[index]
    index += 1
    if index == FRAME_CNT:
        index = 0

    root.geometry(f'100x100+{location}+100') 
    label.configure(image=frame)
    root.after(100, update, index)
    print(location)


root.config(highlightbackground='black')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor','black')

label = tk.Label(root)
label.pack()

root.after(0, update, 0)
root.mainloop()