class AppCore:
    def __init__(self):
        self.is_running = True

    def exit_program(self):
        print("Wychodzenie z programu...")
        self.is_running = False