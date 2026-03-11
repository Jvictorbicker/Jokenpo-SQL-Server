import BOT
import Player
from enum import Enum

class Jogada(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3

def jogadas():
    if ((BOT.choose() == "PEDRA" and Player.chose())):