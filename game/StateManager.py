class StateManager:
    def __init__(self):
        self.current_state = "main_menu"
        self.restart = False

    def change_state(self, new_state):
        self.current_state = new_state
    
    def reset(self, new_restart):
        self.restart = new_restart 
