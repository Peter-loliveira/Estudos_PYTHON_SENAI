from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, genero, peso, raca, tipo_pelo):
        super().__init__(nome, idade, genero, peso)
        self._raca = raca
        self._tipo_pelo = tipo_pelo
        super().som = 'Latido'

    def obter_informacoes(self):
        return super().obter_informacoes() + '\Raça: {} | Tipo de Pelo:{}\n'.format(self.raca,self.tipo_pelo)
    
    @property
    def raca(self):
        return self._raca
    @raca.setter
    def raca(self,raca_informada):
        self._raca = raca_informada
    
    @property
    def tipo_pelo(self):
        return self._tipo_pelo
    @tipo_pelo.setter
    def tipo_pelo(self,tipo_pelo_informada):
        self._tipo_pelo = tipo_pelo_informada