import random

class Response:
    def __init__(self,dictionary):
        self.dictionary = dictionary

class Repeat(Response):
    def response(self,input):
        return '{}とはなに？'.format(input)
class Random(Response):
    def response(self,input):
        return random.choice(self.dictionary.random)
