import pynput

def block_mouse():
    global mouse_listener
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()

def enable_mouse():
    global mouse_listener
    mouse_listener.stop()

def block_keyboard():
    global keyboard_listener
    keyboard_listener = pynput.keyboard.Listener(suppress=True)
    keyboard_listener.start()
    
def enable_keyboard():
    global keyboard_listener
    keyboard_listener.stop()
