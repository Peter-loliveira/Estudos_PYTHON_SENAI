"""
1. Possui o atributo de instância raio.
2. Possui o atributo de classe pi = 3.14.
3. Possui os métodos de instância obter_area() e obter_circunferencia(), que retornam, respectivamente, os valores de área e circunferência.
4. Possui o método de classe atualizar_pi(novo_valor), para atualizar o atributo de classe pi com o novo_valor.
Lembrando que:
Área do Círculo: pi x raio
Circunferência do Círculo: 2 x pi x raio
"""

class circulo:
    pi = 3.14

    def __init__(self, raioDigitado):
        self.raio = raioDigitado
    
    def obter_area(self):
        return self.pi * self.raio
    
    def obter_circunferencia(self):
        return self.pi * self.raio * 2
    
    @classmethod
    def alterarPi(cls, NovoPi):
        cls.pi = NovoPi