from random import random

class Cell :
    def __init__(self):
        self.alive = False

    def make_alive(self):
        self.alive = True

    def make_dead(self):
        self.alive = False

    def is_alive(self):
        return self.alive
