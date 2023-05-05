import json
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
  "{ 'to': 'writer', 'from': 'user' } I would like you to work with an agent named 'editor' and request they critique your work. " + \
  "Write subsequent drafs to incorporate their suggestions and resubmit for further input. " + \
  "Lets start by writing a detailed scene decription of a fantasy woodland nook near a stream."

def extract_recipient(last_response):
    routing_data = last_response[last_response.find("{"):last_response.rfind("}")+1]
    routing_data = routing_data.replace("'", "\"")
    print("routing: " + routing_data)
    routing = json.loads(routing_data)
    recipient = routing["to"]
    return recipient

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
      recipient = extract_recipient(last_response)
      for agent in agents:
        if (agent in recipient):
          last_response = agents[agent].generate_text(last_response)
          break
