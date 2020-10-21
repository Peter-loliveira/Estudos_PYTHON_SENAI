from Jogo import jogo
from random import shuffle

class JogoCartas(jogo):
    def __init__(self, nome, classificacao_etaria, preco, tipo, nr_jogadores, deck):
        super().__init__(nome, classificacao_etaria, 1, preco)
        self._qtd_jogadores = nr_jogadores
        self._deck = []
        self.dados_jogo
    
    @property
    def qtd_jogadores(self):
        return self.qtd_jogadores
    @qtd_jogadores.setter
    def qtd_jogadores(self, jogadores):
        self._qtd_jogadores = jogadores

    @property
    def deck(self):
        return self._deck
    @deck.setter
    def deck(self, CartasDeck):
        self._deck = CartasDeck

    def embaralhar(self, deck):
        return shuffle(deck)

    