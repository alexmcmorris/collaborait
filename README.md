# COLLABOR**ai**T

### A multi-agent AI collaboration prototype

Welcome to the poorly named collaborative brainstorming with ChatGPT agents project! This Python-based project aims to help developers and brainstormers alike collaborate more effectively by utilizing ChatGPT-powered agents that interact with each other to provide valuable insights and suggestions.

## Overview

This project was born out of the desire for more interactivity in the development process, as well as a way to improve upon existing AI-based tools. The current implementation features a few predefined agents set up in a loop that communicate using a simple JSON format tag.

## How it works

Requests begin with JSON data for routing. The format is as follows:
```
{ 'to': 'writer', 'from': 'whatever' }
```

Start with routing data for the writer agent followed by a prompt for the writer agent. Ask the agent to create a draft on an interesting topic and to sends it to 'editor' for review. This will get the writer to start things off. Inspect the generated response for the proper routing data declaring the editor agent as the recipient. If everything looks good, just hit **[Enter]** to send it according to the routing data.

The agents will take turns responding to each other. As long as the responses starts with a to/from tag in the routing data, press **[Enter]** to send it to the correct agent. In case the writer agent doesn't provide a draft and merely thanks the editor, you can impersonate the editor and ask that the writer send the latest draft. If the recipient tag is incorrect, use the command **forward@agent_name** to forward the message to the intended recipient. Things will often work themselves out after that.

## Current State and Future Plans

At the moment, the project is in its early stages, with the writer and editor agents functioning with some fragility. The moderator agent has been added as an experiment to help direct the conversation and provide flow control but is not yet integrated into the decision-making process.

Our ultimate goal is to create a dynamic "chat room" where multiple agents can interact and provide meaningful feedback from various perspectives. This would enable users to discuss project design ideas at any level, accompanied by idea bots, moderators, note-takers, and other AI-driven participants.

As the project evolves, we plan to:

- Incorporate a summary feature for third parties to listen to conversations in the "room"
- Improve agent interactions and decision-making abilities
- Add more diverse agents with distinct personalities and roles
- We hope you find this project intriguing and useful for your brainstorming and collaboration needs. Any feedback, suggestions, and contributions are greatly appreciated as we continue to refine and expand the functionality of these AI-driven agents. Happy collaborating!

## Sample Output

Here is some sample output, using the default prompt I just kept pressing enter:

PS D:\AI\collaborait> python main.py

> Last response: { 'to': 'writer', 'from': 'user' } I would like you to work with an agent named 'editor' and request they critique your work. Write subsequent drafs to incorporate their suggestions and resubmit for further input. Lets start by writing a detailed scene decription of a fantasy woodland 
nook near a stream.

Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit

Enter command:

routing: { "to": "writer", "from": "user" }

> Last response: { 'to': 'editor', 'from': 'writer' } Can you please review my scene description of a fantasy woodland nook near a stream? I would love your feedback on how to make it more engaging and immersive.
>
> The woodland nook was tucked away beneath the gnarled roots of a towering oak tree, which seemed to provide a protective canopy over the small clearing. The sound of a burbling stream could be heard nearby, and a gentle breeze carried the sweet scent of wildflowers through the air. The ground was soft and spongy beneath my feet, covered in a lush carpet of emerald green moss and delicate ferns. Sunlight filtered through the leaves of the oak tree, dappling the clearing with shifting patterns of light and shadow. At the center of the nook was a small pond, shimmering with the colors of the surrounding foliage. It was a peaceful and enchanting place, where one could easily lose track of time and immerse themselves in the natural beauty of the world.
>
> Looking forward to your thoughts and suggestions on how I can bring this scene to life even more!

Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit

Enter command:

routing: { "to": "editor", "from": "writer" }

> Last response: { 'to': 'writer', 'from': 'editor' }
>
> Great job setting the scene! This is a lovely start, and I can definitely picture the woodland nook in my mind. Here are a few suggestions to make it even more immersive:
>
> 1. Use sensory details: You've done a great job describing the visual aspects of the nook, but what about the other senses? For example, what does the water in the stream sound like? Is it a gentle trickle or a rushing current? What about the wildflowers - do they have a distinct scent that the character can smell? By adding in sensory details, you can transport the reader even more fully into the scene.
>
> 2. Add in some movement: Right now, the scene is quite still. Consider adding in some movement to make it feel more dynamic. For example, maybe a butterfly flits by, or a fish jumps out of the pond. These small movements can add a sense of life and activity to the scene.
>
> 3. Consider the character's emotional response: How does the character feel when they enter this nook? Are they in awe of the beauty around them, or do they feel a sense of peace and calm? By giving the character an emotional response, you can help the reader connect even more deeply with the setting.
>
> Overall, great job! With a few tweaks, this scene could be even more immersive and engaging. Let me know if you have any questions or would like more specific feedback!

Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit

Enter command:

routing: { "to": "writer", "from": "editor" }

> Last response: { 'to': 'editor', 'from': 'writer' }
>
> Thank you for your suggestions, they are really helpful! Here's a revised version of the scene that incorporates your feedback:
>
> As I stepped into the woodland nook, the sound of the stream caught my attention. It was a gentle, soothing sound, like a lullaby. The scent of the wildflowers surrounded me, and I breathed in deeply, taking in their sweet fragrance. As I walked towards the pond, I noticed a butterfly fluttering by, 
its wings a blur of color against the green foliage.
>
> The shimmering colors of the pond drew me in, and I felt a sense of awe at the natural beauty before me. The gentle movement of the water created ripples that danced across the surface, reflecting the shifting patterns of light and shadow from the leaves above. The spongy ground beneath my feet seemed to cushion my steps, and I felt a sense of peace and calm wash over me.
>
> I sat down on the mossy bank of the pond and closed my eyes, taking in all the sensory details around me. The sound of the stream, the scent of the wildflowers, the gentle movement of the water - they all combined to create a sense of harmony and tranquility that enveloped me. It was a magical place, a world apart from the chaos and stress of everyday life.
>
> Let me know what you think!

Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit

Enter command:

routing: { "to": "editor", "from": "writer" }

> Last response: { 'to': 'writer', 'from': 'editor' }
>
> Wow, this is a fantastic revision! You've really brought the scene to life with your use of sensory details and movement. I love how you've incorporated the butterfly, which adds a small but meaningful touch of life and movement to the scene.
>
> Your description of the pond is also beautifully done - the way you've described the movement and reflections of the water is very immersive. And by giving the character an emotional response to the setting, you've made it even more engaging for the reader.
>
> Overall, this version of the scene is much more vivid and immersive than the original. Fantastic job incorporating my suggestions!

Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit

Enter command:

routing: { "to": "writer", "from": "editor" }

> Last response: { 'to': 'user', 'from': 'writer' }
>
> Thank you for your helpful input, and thank you to the editor for their excellent suggestions. I'm glad to hear that my revised scene description of the fantasy woodland nook near a stream was successful in bringing the reader into the scene. It was a pleasure working with you both, and I look forward to collaborating further on this project.

Format: { 'to': 'agent_name' } [prompt], forward@agent_name, quit

Enter command:
