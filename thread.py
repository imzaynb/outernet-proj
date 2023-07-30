import threading

class RunCommandsAsync(threading.Thread):
    def __init__(self, tk_root, commands):
        super().__init__()
        self.tk_root = tk_root
        self.commands = commands
        self.start()

    def run(self):
        running: bool = True
        once: bool = True
        while running:
            if once:
                for function in self.commands:
                    function()
                once = False
            