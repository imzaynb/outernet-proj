import webbrowser
import pyautogui
import time
from sys import platform

def type_words(str, increment=0):
    for x in str:
        pyautogui.typewrite(x)
        time.sleep(increment)

def type_words_into_tab(website: str, text: str):
    webbrowser.open_new_tab(website)
    time.sleep(3)
    type_words(text)

def rick_roll(website: str = "https://www.youtube.com/watch?v=xm3YgoEiEDc"):
    webbrowser.open_new_tab(website)

def win_closing():      
    if platform == "win32":
        import win32gui, win32con

        def callback(hwnd, extra):
            if win32gui.IsWindowVisible(hwnd):
                print(f"Window text: '{win32gui.GetWindowText(hwnd)}'")

        def minimize_everything(hwnd, extra):
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

        win32gui.EnumWindows(minimize_everything, None)

    else:
        type_words_into_tab("you think you may have bested me by not using Michealsoft Binbows®, but fear not HAHHAAHAHA")

if __name__ == "__main__":
    win_closing()
    rick_roll("https://www.youtube.com/watch?v=xm3YgoEiEDc")