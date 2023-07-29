import webbrowser
import pyautogui, time
import sys
import termios
import contextlib


STD_INCREMENT = 0.0001
def type_words(str, increment=STD_INCREMENT):
    for x in str:
        pyautogui.typewrite(x)
        time.sleep(increment)

webbrowser.open_new_tab("google.com")
time.sleep(1)

type_words("I Like Turtles... DO YOU like Turtles??")

