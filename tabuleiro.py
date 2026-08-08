class Tabuleiro:
    def __init__(self):
        self.casas = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


    def exibir(self):
        for casa in self.casas:
            print(casa)


    def verificar_vitoria(self):
        for casa in self.casas:

            # São varias condições na verdade.
            # Lembrese da horizontal e da de coluna
            condicao = (
                casa[0] != ' ' and
                casa[0] == casa[1] and
                casa[1] == casa[2]
            )

            if condicao:
                print(f"O jogador do símbolo {casa[0]} VENCEU")
                break

        print("Não temos vencedores.")

    def verificar_empate(self):
        ...
    

    def jogar(self, linha: int, coluna: int, simbolo: str):
        if (linha > 3 or linha < 1) or (coluna > 3 or coluna < 1):
            raise ValueError('ERRO: Por favor, passe linhas ou colunas válidas')

        try:
            print("SUA JOGADA:\n")

            #TODO Validação para não permtir que seja jogado em uma casa já preenchida (def casa livre)

            self.casas[linha - 1][coluna - 1] = simbolo

            self.exibir()

            print("\n\n")
            
        except TypeError:
            print("ERRO: A linha ou coluna devem ser do tipo inteiro")

    def casa_livre():
        ...
        

if __name__ == '__main__':
    t = Tabuleiro()

    t.jogar(3, 1, 'O')
    t.exibir()
    t.verificar_vitoria()
    t.jogar(3, 1, 'O')
    t.jogar(3, 1, 'O')

    