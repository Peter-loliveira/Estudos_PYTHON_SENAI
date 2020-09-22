class Animal:
    def __init__(self,  nome, idade, genero, peso):
        self._nome = nome
        self._idade = idade
        self._genero = genero
        self._peso = peso
        self._energia = 60.0
        self.som = ''

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome_informado):
        self._nome = nome_informado
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade_informada):
        self._idade = idade_informada
    
    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, genero_informado):
        self._genero = genero_informado
    
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self, peso_informado):
        self._peso = peso_informado
    
    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self, energia_informado):
        self._energia = energia_informado

    @property
    def obter_informacoes(self):
        infos = 'Nome: {} | Idade: {} | Genero: {}\n'.format(self.nome,self.idade,self.genero)
        infos = 'Peso: {} kg | Energia: {}\n'.format(self.peso,self.energia)
        infos = self.emitir_som()
        return infos
    
    def comer(self):
        self.peso += .7
        if self.energia < 75:
            self.energia += 25
        else:
            self.energia = 60
    
    def mover(self):
        self.peso -+ .1
        if self.energia > 20:
            self.energia -= 10
    
    def emitir_som(self):
        if self.energia > 10:
            self.energia -= 5
            return 'Som do cão {}: {}\n'.format(1,2)
        else: 
            return ''
