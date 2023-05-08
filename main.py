import json
from apikey import api_key
from collaborator import Moderator, Writer, Editor
from context import Context
from generator import Generator

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

context = Context()
context.add_message(last_response)

def extract_recipient(message):
    routing_data = message[message.find("{") : message.rfind("}")+1]
    routing_data = routing_data.replace("'", "\"")
    print("routing: " + routing_data)
    routing = json.loads(routing_data)
    recipient = routing["to"]
    return recipient

def send_message(recipient, message):
    print("Sending to: " + recipient)
    if (recipient in agents):
       response = agents[recipient].generate_text(message)
       print("Response: " + response)
       context.add_message(response)

def dispatch_message(message):
    print("Dispatching message: " + message)
    recipient = extract_recipient(message)
    send_message(recipient, message)

while True:
    print("Last response: " + context.get_last_message())
    print(command_help)
    user_input = input("Enter command: ")
    user_input = user_input.lower()
    
    if user_input == "quit":
       break
    
    elif "forward@" in user_input:
      recipient = user_input[user_input.find("@")+1 : ]
      send_message(recipient, context.get_last_message())
    
    elif "'to':" in user_input:
      dispatch_message(user_input)

    elif user_input is None or len(user_input) == 0:
      dispatch_message(context.get_last_message())
