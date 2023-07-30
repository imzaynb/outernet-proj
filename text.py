import pyautogui
import time
import subprocess

def draw_circle(x, y, radius):
    pyautogui.moveTo(x, y)
    pyautogui.dragRel(-radius, radius, duration=0.5)  # Draw the circle's bottom side

def draw_oval(x, y, width, height):
    pyautogui.moveTo(x, y)
    pyautogui.dragRel(width, height, duration=0.5)  # Draw the oval's right side


def ms_paint():
    # Open Paint using the 'mspaint' command in the background
    subprocess.Popen(['mspaint'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for Paint to start (adjust the delay if needed)
    time.sleep(3)

    # Send the Alt + Space keys to open the window's system menu
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.5)

    # Send the 'x' key to maximize the window (toggle full screen)
    pyautogui.press('x')
    time.sleep(0.5)


    #pick the circle tool
    for i in range(19):
        pyautogui.press('tab')
    pyautogui.press("right")
    pyautogui.press("right")
    pyautogui.press("enter")


    # Draw the first circle
    draw_circle(400, 400, 50)

    # Move to draw the second circle (40 pixels below the first circle)
    pyautogui.moveRel(0, 40, duration=0.5)

    pyautogui.click()

    # Draw the second circle
    draw_circle(400, 510, 50)

    # Move to draw the second circle (40 pixels below the first circle)
    pyautogui.moveRel(0, 40, duration=0.5)

    pyautogui.click()

    # Move to draw the oval between the circles
    pyautogui.moveTo(325, 420, duration=0.5)

    # Draw the oval between the circles
    draw_oval(325, 440, 400, 80)

    # Click out of the oval
    pyautogui.moveRel(100, 100)
    pyautogui.click()

    # Select the text box tool
    for i in range(15):
        pyautogui.press('tab')
        time.sleep(0.1)
    pyautogui.press('enter')

    # Draws the textbox
    draw_oval(325, 440, 400, 80)

    # Changes the font size
    pos = pyautogui.position()
    pyautogui.click(828, 221)
    pyautogui.write("32")

    # Types the message
    pyautogui.moveTo(pos)
    pyautogui.moveRel(-50, -50)
    pyautogui.click()
    pyautogui.write("Test text")

if __name__ == "__main__":
    ms_paint()
