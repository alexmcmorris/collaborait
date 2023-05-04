from generator import Generator
from collaborator import Moderator, Writer, Editor
from apikey import api_key

model = "gpt-3.5-turbo"
generator = Generator(model, api_key)

agents = \
{
  "moderator": Moderator(generator),
  "writer": Writer(generator),
  "editor": Editor(generator)
}

command_help = "Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit"

last_response = \
  "{ 'to': 'writer', } I would like you to work with an agent named 'editor' and write a short poem and tell them to critique your work. " + \
  "Write subsequent drafs to incorporate their suggestions and resubmit for further input. " + \
  "Lets start by writing a beautiful short poem about a grain of sand on the beach."

last_response = ""
while True:
    print("Last response: " + last_response)
    print(command_help)
    user_input = input("Enter command: ")
    user_input = user_input.lower()
    if user_input == "quit":
        break
    if "'to':" in user_input:
      for agent in agents:
        if (agent in user_input):
          last_response = agents[agent].generate_text(user_input)
          break
    if "forward@" in user_input:
       for agent in agents:
          if (agent in user_input):
            last_response = agents[agent].generate_text(last_response)
            break
    if user_input is None or len(user_input) == 0:
      for agent in agents:
        if (agent in last_response):
          last_response = agents[agent].generate_text(last_response)
          break

# first_draft = writer_agent.generate_text(prompt)
# first_review = editor_agent.generate_text(first_draft)
# second_draft = writer_agent.generate_text(first_review)
# second_review = editor_agent.generate_text(second_draft)
# response = writer_agent.generate_text(second_review)
# print(response)
