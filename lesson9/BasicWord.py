import random

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class BasicWord:

    def __init__(self):
        self.response = requests.get("https://jsonkeeper.com/b/68VA", verify=False).json()
        self.words = self.response.keys()
        self.items = self.response.values()

    def is_correct(self, user_answer):
        if user_answer.lower() in self.items:
            return True
        else:
            return  False

    def count_subwords(self):
        return len(self.items)

    def __repr__(self):
        return random.choice(self.words)

word = BasicWord()


