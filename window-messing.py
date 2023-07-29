import webbrowser, pyautogui, time

STD_INCREMENT = 0.0000
def type_words(str, increment=STD_INCREMENT):
    for x in str:
        pyautogui.typewrite(x)
        time.sleep(increment)

def type_in_tab():
    webbrowser.open_new_tab("google.com")
    time.sleep(3)

    type_words("You got fucked lol... HAHHAHAHHAHA")

if __name__ == "__main__":
    type_in_tab()