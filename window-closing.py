from sys import platform

def win_closing():      
    if platform == "win32":
        import win32gui, win32con

        def callback(hwnd, extra):
            if win32gui.IsWindowVisible(hwnd):
                print(f"Window text: '{win32gui.GetWindowText(hwnd)}'")

        def minimize_everything(hwnd, extra):
            if win32gui.IsWindowVisible(hwnd)and win32gui.GetWindowText(hwnd) != '':
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

        win32gui.EnumWindows(minimize_everything, None)

    if "linux" in platform:
        ...


if __name__ == "__main__":
    win_closing()