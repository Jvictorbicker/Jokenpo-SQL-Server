class player:
    def __init__(self,escolha):
        self.escolha = escolha

    def chose(self):
        while True:
            print("""
            [1] PEDRA
            [2] PAPEL
            [3] TESOURA
            [4] SAIR
            ----------------------
            """)

            escolha = int(input("Digite sua escolha: "))


            if escolha == 1:
                return 1
            elif escolha == 2:
                return 2
            elif escolha == 3:
                return 3
            elif escolha == 4:
                print("Obrigado por jogar!!")
                return False