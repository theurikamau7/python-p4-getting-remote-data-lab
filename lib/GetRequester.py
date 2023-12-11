import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = self.get_response_body()
        # Decode bytes to string
        content_string = response.decode('utf-8')
        # Load JSON from the string
        return json.loads(content_string)