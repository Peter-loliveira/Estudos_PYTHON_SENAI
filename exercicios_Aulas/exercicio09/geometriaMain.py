""" 
É o módulo que vai possuir a função main e iniciar o programa.
1Q. Crie pelo menos um objeto Quadrado, passando o lado como parâmetro.
2Q. Chame os métodos criados em Quadrado para imprimir os valores de área, perímetro e diagonal do objeto.
3Q. Em seguida, chame o método de classe atualizar_diag() e passe como parâmetro o valor de sqrt(2) do módulo math.
4Q. Imprima novamente o valor da diagonal.

1C. Crie pelo menos um objeto Circulo, passando o raio como parâmetro.
2C. Imprima os valores de área e circunferência do objeto antes de atualizar pi.
3C. Em seguida, chame o método de classe atualizar_pi() e passe como parâmetro o valor de pi do módulo math.
4C. Imprima novamente os valores de área e circunferência.
"""
from quadrado import quadrado
from circulo import circulo
from math import pi, sqrt

def main():


    NovoQuadrado = quadrado(float(input('\nInforme o tamanho do LADO do Quadrado: ')))
    print('\nO QUADRADO tem os seguintes valores:')
    print('Area: {:.2f}'.format(NovoQuadrado.obter_area()))
    print('Perimetro: {:.2f}'.format(NovoQuadrado.obter_perimetro()))
    print('Diagonal: {:.2f}'.format(NovoQuadrado.obter_diagonal()))
    print('###########################')
    print('# CORRIGINDO RAIZ DE DOIS #')
    print('###########################')
    NovoQuadrado.atualizar_RaizDois(sqrt(2))
    print('\nAGORA O quadrado tem a seguinte DIAGONAL:')
    print('Diagonal: {:.2f}'.format(NovoQuadrado.obter_diagonal()))

    print('\n___________________________________________________\n')
    NovoCirculo = circulo(float(input('Informe o tamanho do RAIO do circulo: ')))
    print('Área: {:.2f}'.format(NovoCirculo.obter_area()))
    print('Circunferencia: {:.2f}'.format(NovoCirculo.obter_circunferencia()))
    print('##########################')
    print('# CORRIGINDO VALOR DE PI #')
    print('##########################')
    NovoCirculo.alterarPi(pi)
    print('\nAGORA o circulo tem a Circunferencia: {:.2f}'.format(NovoCirculo.obter_circunferencia()))

main()