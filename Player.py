from Jogadas import Jogada

class Player:
    def __init__(self):
        self.escolha = None

    def chose(self):
        while True:
            print("""
            [1] PEDRA
            [2] PAPEL
            [3] TESOURA
            [4] SAIR
            ----------------------
            """)

            try:
                escolha = int(input("Digite sua escolha: "))
            except ValueError:
                print("Por favor, digite um número válido!")
                continue

            if escolha == 4:
                print("Obrigado por jogar!!")
                return None

            try:
                self.escolha = Jogada(escolha)
                return self.escolha
            except ValueError:
                print("Opção inválida, tente novamente!")
