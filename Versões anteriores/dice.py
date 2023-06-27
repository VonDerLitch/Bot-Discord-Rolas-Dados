from random import randint

class Roller:
    def __init__(self,n_lados: int):
        self.lados = [i for i in range(1, n_lados + 1)]
        self.log_path = '/logs'
    
    def jogar(self,n_jogadas):
        if not isinstance(n_jogadas, int):
            raise Exception('O número de jogadas deve ser informado em formato inteiro')
        
        print(f'Jogando {n_jogadas} dados.')
        for i in range(1, n_jogadas + 1):
            res = randint(self.lados[0], self.lados[-1])
            jogada = f'Jogada de número {i}: {res}!'
            print(jogada)

    