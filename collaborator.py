from directives import ModeratorDirective, WriterDirective, EditorDirective

class Collaborator:
    def __init__(self, generator, directive):
        self.generator = generator
        self.directive = directive
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def reset_messages(self):
        self.messages = []

    def generate_text(self, prompt):
        self.add_message("user", prompt)
        message = self.generator.generate(self.directive.build(), self.messages)
        if (message is None):
            print("No response")
            return None
        self.add_message('system', message)
        return message

class Moderator(Collaborator):
    def __init__(self, generator):
        super().__init__(generator, ModeratorDirective())

class Writer(Collaborator):
    def __init__(self, generator):
        super().__init__(generator, WriterDirective())

class Editor(Collaborator):
    def __init__(self, generator):
        super().__init__(generator, EditorDirective())
