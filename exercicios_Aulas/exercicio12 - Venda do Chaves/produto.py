class produto():
    _preco_tamanho = [2,2.5,3]

    def __init__(self, nome, sabor, tamanho, preco_base):
        self._nome = nome
        self._sabor = sabor
        self._tamanho = tamanho
        self._preco_base = preco_base
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_Nome):
        self._nome = novo_Nome
    
    @property
    def sabor(self):
        return self._sabor
    @sabor.setter
    def sabor(self, novo_sabor):
        self._sabor = novo_sabor
    
    @property
    def tamanho(self):
        return self._tamanho
    @tamanho.setter
    def tamanho(self, novo_tamanho):
        self._tamanho = novo_tamanho
    
    @property
    def preco_base(self):
        return self._preco_base
    @preco_base.setter
    def preco_base(self, novo_preco_base):
        self._preco_base = novo_preco_base
    
    
    @classmethod
    def preco_tamanho(cls):
        return cls._preco_tamanho

    def preco(self, tamanho):
        return self.preco_base * preco_tamanho[tamanho]
    
    def info(self):
        if self.tamanho == 0:
            TamanhoSelecionado = 'Pequeno'
        elif self.tamanho == 1:
            TamanhoSelecionado = 'Medio'
        elif self.tamanho == 2:
            TamanhoSelecionado = 'Grande'
        
        return 'Nome: {}\nSabor: {}\nTamanho: {}\nPreço: {}'.formart(
            self.nome, self.sabor, TamanhoSelecionado, self.preco(self.tamanho)
        )