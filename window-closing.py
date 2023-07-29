import pyautogui

def close_window():
    button_rect = pyautogui.locateOnScreen("x_button.png", confidence=0.8, grayScale=True)
    if not button_rect: continue

    button_center = pyautogui.center()
    pyautogui.click(x=button_center.x, y=button_center.y)

