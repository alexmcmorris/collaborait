import requests
import json

class Generator:
    def __init__(self, model, api_key, temperature=0.7, max_tokens=1536):
        self.model = model
        self.api_key = api_key
        self.temperature = temperature
        self.max_tokens = max_tokens
        
    def generate(self, direction, summary):
        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.api_key
        }
        data = {
            'model': self.model,
            'messages': [{"role": "system", "content": direction }] + summary,
            'max_tokens': self.max_tokens,
            'temperature': self.temperature
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            completions = response.json()['choices']
            message = completions[0]['message']['content'].strip()
            return message
        else:
            print('Error generating text:', response.text)
            return None
