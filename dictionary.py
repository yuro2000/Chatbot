import random

class Dictionary:
    def __init__(self):
        self.random = []
        rfile = open('random.txt','r')
        lines = rfile.readlines()
        rfile.close()

        for line in lines:
            str = line.rstrip('\n')
            if (str!=''):
                self.random.append(str)
