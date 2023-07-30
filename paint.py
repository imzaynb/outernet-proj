import pyautogui
import time
import subprocess
import numpy as np
import matplotlib.pyplot as plt

M = 1000
angle = np.exp(1j * 2 * np.pi / M)
angles = np.cumprod(np.ones(M + 1) * angle)
x, y = np.real(angles), np.imag(angles)
plt.plot(x, y)

def draw_circle(x, y, radius):
    angle = 0
    while angle < 360:
        x_offset = int(radius * (0.999 * angle) / 180)
        y_offset = int(radius * (0.999 * angle) / 180)
        pyautogui.click(x + x_offset, y + y_offset)
        angle += 10
        time.sleep(0.05)

def draw_oval(x, y, width, height):
    angle = 0
    while angle < 360:
        x_offset = int(width * (0.999 * angle) / 180)
        y_offset = int(height * (0.999 * angle) / 180)
        pyautogui.click(x + x_offset, y + y_offset)
        angle += 10
        time.sleep(0.05)

def main():
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

    # Draw the first circle
    draw_circle(200, 200, 50)

    # Move to draw the second circle
    pyautogui.moveTo(350, 200)
    time.sleep(1)

    # Draw the second circle
    draw_circle(350, 200, 50)

    # Move to draw the oval
    pyautogui.moveTo(250, 400)
    time.sleep(1)

    # Draw the oval
    draw_oval(250, 400, 100, 60)

if __name__ == "__main__":
    main()
