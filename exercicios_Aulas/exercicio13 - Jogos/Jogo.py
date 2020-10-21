class jogo():
    _tipos_jogo = ['Jogo Eletrônico', 'Jogo de Cartas', 'Outro']

    def __init__(self, nome, classificacao_etaria, tipo, preco):
        self._nome = nome
        self._clas_etaria = classificacao_etaria
        self._tipo = self.tipos_jogo[tipo]
        self.preco = preco
    
    @property
    def tipos_jogo(self):
        return self._tipos_jogo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, NomeJogo):
        self._nome = NomeJogo

    @property
    def clas_etaria(self):
        return self._clas_etaria

    @clas_etaria.setter
    def clas_etaria(self, novaIdade):
        self._clas_etaria = novaIdade
        print(novaIdade)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, NovoValor):
        if self.clas_etaria >= 18:
            self._preco = NovoValor * 1.1
        elif 12 >= self.clas_etaria < 18:
            self._preco = NovoValor * 1.05
        else:
            self._preco = NovoValor

    def dados_jogo(self):
        saida = '\nNome: {}\nPreço: {}\nTipo de Jogo: {}'.format(
            self.nome,
            self.preco,
            self._tipo
        )
        return saida
