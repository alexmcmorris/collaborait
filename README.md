# collabor***AI***t
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

Here is some sample output, using the default prompt I just kept pressing enter:
<details><summary>Expand Output</summary>

```
PS D:\AI\collaborait> python main.py
Last response: { 'to': 'writer', 'from': 'user' } I would like you to work with an agent named 'editor' and request they critique your work. Write subsequent drafs to incorporate their suggestions and resubmit for further input. Lets start by writing a detailed scene decription of a fantasy woodland 
nook near a stream.
Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit
Enter command:
routing: { "to": "writer", "from": "user" }
Last response: { 'to': 'editor', 'from': 'writer' } Can you please review my scene description of a fantasy woodland nook near a stream? I would love your feedback on how to make it more engaging and immersive.

The woodland nook was tucked away beneath the gnarled roots of a towering oak tree, which seemed to provide a protective canopy over the small clearing. The sound of a burbling stream could be heard nearby, and a gentle breeze carried the sweet scent of wildflowers through the air. The ground was soft and spongy beneath my feet, covered in a lush carpet of emerald green moss and delicate ferns. Sunlight filtered through the leaves of the oak tree, dappling the clearing with shifting patterns of light and shadow. At the center of the nook was a small pond, shimmering with the colors of the surrounding foliage. It was a peaceful and enchanting place, where one could easily lose track of time and immerse themselves in the natural beauty of the world.

Looking forward to your thoughts and suggestions on how I can bring this scene to life even more!
Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit
Enter command:
routing: { "to": "editor", "from": "writer" }
Last response: { 'to': 'writer', 'from': 'editor' }

Great job setting the scene! This is a lovely start, and I can definitely picture the woodland nook in my mind. Here are a few suggestions to make it even more immersive:

1. Use sensory details: You've done a great job describing the visual aspects of the nook, but what about the other senses? For example, what does the water in the stream sound like? Is it a gentle trickle or a rushing current? What about the wildflowers - do they have a distinct scent that the character can smell? By adding in sensory details, you can transport the reader even more fully into the scene.

2. Add in some movement: Right now, the scene is quite still. Consider adding in some movement to make it feel more dynamic. For example, maybe a butterfly flits by, or a fish jumps out of the pond. These small movements can add a sense of life and activity to the scene.

3. Consider the character's emotional response: How does the character feel when they enter this nook? Are they in awe of the beauty around them, or do they feel a sense of peace and calm? By giving the character an emotional response, you can help the reader connect even more deeply with the setting.

Overall, great job! With a few tweaks, this scene could be even more immersive and engaging. Let me know if you have any questions or would like more specific feedback!
Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit
Enter command:
routing: { "to": "writer", "from": "editor" }
Last response: { 'to': 'editor', 'from': 'writer' }

Thank you for your suggestions, they are really helpful! Here's a revised version of the scene that incorporates your feedback:

As I stepped into the woodland nook, the sound of the stream caught my attention. It was a gentle, soothing sound, like a lullaby. The scent of the wildflowers surrounded me, and I breathed in deeply, taking in their sweet fragrance. As I walked towards the pond, I noticed a butterfly fluttering by, 
its wings a blur of color against the green foliage.

The shimmering colors of the pond drew me in, and I felt a sense of awe at the natural beauty before me. The gentle movement of the water created ripples that danced across the surface, reflecting the shifting patterns of light and shadow from the leaves above. The spongy ground beneath my feet seemed to cushion my steps, and I felt a sense of peace and calm wash over me.

I sat down on the mossy bank of the pond and closed my eyes, taking in all the sensory details around me. The sound of the stream, the scent of the wildflowers, the gentle movement of the water - they all combined to create a sense of harmony and tranquility that enveloped me. It was a magical place, a world apart from the chaos and stress of everyday life.

Let me know what you think!
Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit
Enter command:
routing: { "to": "editor", "from": "writer" }
Last response: { 'to': 'writer', 'from': 'editor' }

Wow, this is a fantastic revision! You've really brought the scene to life with your use of sensory details and movement. I love how you've incorporated the butterfly, which adds a small but meaningful touch of life and movement to the scene.

Your description of the pond is also beautifully done - the way you've described the movement and reflections of the water is very immersive. And by giving the character an emotional response to the setting, you've made it even more engaging for the reader.

Overall, this version of the scene is much more vivid and immersive than the original. Fantastic job incorporating my suggestions!
Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit
Enter command:
routing: { "to": "writer", "from": "editor" }
Last response: { 'to': 'user', 'from': 'writer' }

Thank you for your helpful input, and thank you to the editor for their excellent suggestions. I'm glad to hear that my revised scene description of the fantasy woodland nook near a stream was successful in bringing the reader into the scene. It was a pleasure working with you both, and I look forward to collaborating further on this project.
Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit
Enter command:

```
</details>