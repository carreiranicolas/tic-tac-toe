class Jogador:
    def __init__(self, nome: str, simbolo: str):
        self.nome = nome.lower().capitalize()
        self.simbolo = simbolo.upper()

    def escolher_jogada(self, linha: int, coluna: int):
        ...

if __name__ == '__main__':
    ...