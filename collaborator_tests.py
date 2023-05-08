import unittest
from collaborator import Collaborator

class CollaboratorTests(unittest.TestCase):
    def test_extract_recipient(self):
        last_response = "{ 'to': 'writer', 'from': 'user' } I would like you to work with an agent named 'editor' and request they critique your work. " + \
        "Write subsequent drafs to incorporate their suggestions and resubmit for further input. " + \
        "Lets start by writing a detailed scene decription of a fantasy woodland nook near a stream."
        collaborator = Coll
        recipient = Collaborator.extract_recipient(last_response)
        self.assertEqual(recipient, "writer")