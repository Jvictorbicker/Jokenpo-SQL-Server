from Player import Player
from BOT import Bot
from Jogadas import Jogada


def win(player_choice, bot_choice):
    print(f"Bot escolheu: {bot_choice.name}")

    if bot_choice == player_choice:
        return "Empate!"

    winning = {
        Jogada.PEDRA: Jogada.TESOURA,
        Jogada.PAPEL: Jogada.PEDRA,
        Jogada.TESOURA: Jogada.PAPEL,
    }

    if winning[bot_choice] == player_choice:
        return "Você perdeu!"
    else:
        return "Você ganhou!"


def start():
    player = Player()
    bot = Bot()

    while True:
        escolha = player.chose()

        if escolha is None:
            break

        result = win(escolha, bot.choose())
        print(result)


if __name__ == '__main__':
    start()