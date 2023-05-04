# <span style="color:blue">collaborait</span>
A multi-agent AI collaboration prototype

First Python project so be kind. This is just a little tool to poke at the ChatGPT API.

So it all started because I always poke around with developing something random and want more interactivity than scouring tutorials and whatnot. Then AI comes along and since Copilot X is ghosting me and many of the online interfaces lack context and polish. I figured I could throw my contextless unpolished mess in here too.

It's pretty raw right now. I have it set up in a loop with a few predefined agents. There is a clunky JSON format tag for declaring the recipient. The agents are all instructed to use the same format.

When you start out, begin by prompting the writer to write something:
{ 'to': 'writer', 'from': 'whatever' } Please write something really cool about some interesting topic. Send the first draft to 'editor' for review.

Then it will do just that. If the response begins with a to/from tag just hit enter and it will send it to the correct agent. Rinse and repeat.

Sometimes the writer doesn't like to actually write the draft and just thanks the editor for the suggestions. You can fake a message from the editor to ask for the next draft.

If the to tag is wrong you can use the command 'forward@agent_name' to force send it to them.

I've added a moderator recently. That's just an experiment to see if I can use another agent to help direct the conversation if it stalls as well as translate the messages into flow control back on the programming side. The moderator isn't wired up to any decision making in the app yet. Ultimately, I want the moderator to be able to provide collate a running summary of the conversation to minimize the overall token usage in long conversations.

So, to recap, I only have the writer and editor working currently, and with extreme fragility at that. It's all still two-entity interactions too. I want to incorporate the summary idea so that 3rd parties can listen to the others in the "room" as well. That way they can provide meaningful feedback from their perspectives.

I would love to sit in a "chat room" effectively and talk through project design ideas at any level. Throw a few idea bots in there. A moderator, a notes taker. Maybe even tailor some to be hot-head young punks with fresh ideas and some old crustys to help keep things grounded. Dunno... just brain dribble so far.
