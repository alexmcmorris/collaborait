class Context:
    def __init__(self):
        self.messages = []
        pass

    def add_message(self, message):
        self.messages.append(message)

    def reset_messages(self):
        self.messages = []

    def get_messages(self):
        return self.messages
    
    def get_last_message(self):
        return self.messages[-1]
    
    