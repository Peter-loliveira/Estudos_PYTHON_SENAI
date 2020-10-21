from Jogo import jogo
from JogoCartas import JogoCartas
from JogoEletronico import JogoEletronico

class main():
    jogo1 = jogo('Dominó', 22, 2, 20)
    jogoC = JogoCartas('Yu-Gi-Oh', 12, 40, 1, 2,['Dark Hole', 'Exodia', 'Mirror Force', 'Slifer'])
    jogoE = JogoEletronico('GTA', 18, 0, 150, 'Aventura', ['Windows', 'PlayStation', 'XBox'])

    print(jogo1.dados_jogo())
    print(jogoC.dados_jogo())
    print(jogoE.dados_jogo())

main()