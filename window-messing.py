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

@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


def main():
    print('exit with ^C or ^D')
    with raw_mode(sys.stdin):
        try:
            while True:
                ch = sys.stdin.read(1)
                if not ch or ch == chr(4):
                    break
                print('%02x' % ord(ch),)
        except (KeyboardInterrupt, EOFError):
            pass