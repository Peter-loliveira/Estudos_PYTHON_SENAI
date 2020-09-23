from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, genero, peso, raca, tipo_pelo):
        super().__init__(nome, idade, genero, peso)
        Cachorro.som = 'Latido'
        self._raca = raca
        self._tipo_pelo = tipo_pelo

    def obter_informacoes(self):
        infor = 'Raça: {} | Tipo do Pêlo: {}'.format(self.raca, self.tipo_pelo)
        return super().obter_informacoes() + infor
        # + '\Raça: {} | Tipo de Pelo:{}\n'.format(self.raca,self.tipo_pelo)
    
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