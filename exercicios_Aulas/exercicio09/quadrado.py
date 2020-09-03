'''
1. Possui o atributo de instância lado.
2. Possui o atributo de classe diag = 1.41. (Representa √2)
3. Possui os métodos de instância obter_area() e obter_perimetro() e obter_diagonal(), que retornam os valores das respectivas contas.
4. Possui o método de classe atualizar_diag(novo_valor), para atualizar o atributo de classe diag com o novo_valor.
Lembrando que:
Área do Quadrado = lado x lado
Perímetro do Quadrado = lado x 4
Diagonal do Quadrado = lado x diag
'''
class quadrado:
    RaizDois = 1.41
    def __init__(self,lado_informdo):
        self.lado = lado_informdo
    
    def obter_area(self):
        return self.lado ** 2
    
    def obter_perimetro(self):
        return self.lado *4
    
    def obter_diagonal(self):
        return self.lado * self.RaizDois
    
    @classmethod
    def atualizar_RaizDois(cls, NovaRaisDois):
        cls.RaizDois =  NovaRaisDois