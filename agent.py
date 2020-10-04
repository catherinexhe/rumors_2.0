import random

class Agent:
    def __init__(self, nodeid):
        self.id=nodeid
        self.stories = []
        # fix ^^ later.
    def id(self):
        return self.id

    def receive(self, sentence):
        stories.add(sentence)

    def drop(self):
        sentence = stories[0]
        node = network.getRandomNode()
        node.receive(sentence)

