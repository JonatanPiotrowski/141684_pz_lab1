from config.config import current_language as cl

class AppCore:
    def __init__(self):
        self.is_running = True

    def exit_program(self):
        print(cl["exit_app"])
        self.is_running = False