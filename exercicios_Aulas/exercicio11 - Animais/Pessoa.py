from Animal import Animal

class Pessoa(Animal):
    def __init__(self, nome, idade, genero, peso, naturalidade, ocupacao):
        super().__init__(nome, idade, genero, peso)
        Pessoa.som = 'Fala'
        self._naturalidade = naturalidade
        self.ocupacao = ocupacao
        
        
    def obter_informacoes(self):
        return super().obter_informacoes() 
        + '\nNaturalidade: {} | Ocupacao: {}'.format(self.naturalidade, self.ocupacao)
        + '\nSom do {}: {}'.format(super().nome, super().som)
    
    @property
    def naturalidade(self):
        return self._naturalidade
    @naturalidade.setter
    def naturalidade(self,naturalidade_digitada):
        self._naturalidade = naturalidade_digitada

    @property
    def ocupacao(self):
        return self._ocupacao
    @ocupacao.setter
    def ocupacao(self, ocupacao_digitada):
        if ocupacao_digitada.upper() != 'DOCENTE':
            self._ocupacao = ocupacao_digitada
