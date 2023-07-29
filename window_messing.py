import webbrowser, pyautogui, time
from pynput import keyboard

STD_INCREMENT = 0.0000
def type_words(str, increment=STD_INCREMENT):
    for x in str:
        pyautogui.typewrite(x)
        time.sleep(increment)

def type_in_tab():
    webbrowser.open_new_tab("google.com")
    time.sleep(3)

    type_words("You have been Fucked... HAHAHAHHAHA")

if __name__ == "__main__":
    input("Welcome to your new AI assistant, type any query you want\nyou: ")
    type_in_tab()