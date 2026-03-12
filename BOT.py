import random
from Jogadas import Jogada

class Bot:
    def __init__(self):
        self.escolha = None

    def choose(self):
        self.escolha = Jogada(random.randint(1, 3))
        return self.escolha