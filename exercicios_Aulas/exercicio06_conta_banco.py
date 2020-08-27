'''
Criar uma classe ContaBanco com as seguintes informações:

Atributos
- Nome do banco
- Número da agência
- Número da conta
- Nome do titular
- Tipo (P – Poupança ou C – Corrente)
- Saldo
- Limite de saque

Métodos a serem implementados
- Sacar (valor)
- Depositar (valor)
- Imprimir dados (exibindo os atributos)

Criar a função main() fora da classe e:
- Instanciar um objeto do tipo ContaBanco, definindo valores para os atributos do objeto instanciado
- Realizar depósitos, saques e uma impressão dos dados a partir do objeto de ContaBanco criado
'''

class conta_banco:
    def __init__(self, banco, agencia, conta, titular, tipo, saldo, limite_saque):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.titular = titular
        self.tipo = tipo
        self.saldo = saldo
        self.limite_saque = limite_saque #SE O LIMITE DE SAQUE FOR IGUAL A 0 O CLIENTE TEM VALOR DE SUE ILIMITADO

    def sacar(self, valor):
        self.saldo -= valor
    
    def depositar(self, valor):
        self.saldo += valor

    def alterar_limite(self, valor):
        self.limite_saque = valor
    
    def imprimi_dados(self):
        print('\n#######################')
        print('Dados da Conta\nBanco: {}\nAgencia: {}\nConta: {}\nTitular: {}\nTipo de Conta: {}\nSaldo: {}\nLimite de Saque: {}'.format(self.banco, self.agencia, self.conta, self.titular, self.tipo, self.saldo, self.limite_saque))
        print('#######################\n')
                
def main():
    banco = input('Informe o NOME do banco: ')
    agencia = input('Informe a AGENCIA: ')
    conta = input('Informe a CONTA do banco: ')
    titular = input('Informe o NOME do TITULAR: ')
    tipo = input('Informe o TIPO da conta(Poupança ou Corrente): ')
    limite_saque = float(input('Informe o LIMITE DE SAQUE para essa conta: '))

    conta1 = conta_banco(banco, agencia, conta, titular, tipo, 0, limite_saque)
    
    # MENU DE OPÇÕES
    def menu():
        opcoes = [1,2,3,4,5]
        opcao = -1
        while opcao != 5:
            try:
                opcao = int(input('\nFavor escolha uma das opções abaixo\n1 - Verificar Dados Conta.\n2 - Sacar.\n3 - Depositar.\n4 - Alterar Limite de Saque\n5 - Sair.\n'))
            except:
                    print('\n####################################\nFAVOR DIGITAR UMA OPÇÃO PELO NUMERO!\n####################################')
            else:
                if opcao not in opcoes:
                    print('\n#######################################\nFAVOR DIGITAR UMA DAS OPÇÕES INDICADAS.\n#######################################')
                else:
                    if opcao == 1:
                        conta1.imprimi_dados()
                    elif opcao == 2:
                        realizar_saque()
                    elif opcao == 3:
                        realizar_deposito()
                    elif opcao == 4:
                        alterar_limite_saque()

    # FUNÇÕES DE SAQUE E DEPOSITO
    def realizar_saque():
        print('##################################################')
        try:
            valor_saque = float(input('Digite o valor a ser SACADO: '))
        except:
            print('FAVOR DIGITAR UM VALOR!')
        else:
            if valor_saque > conta1.saldo:
                print('\nSALDO INSUFICIENTE!\n')
            elif valor_saque > conta1.limite_saque and conta1.limite_saque != 0:
                print('\nVALOR ACIMA DO SEU LIMITE DE SAQUE!\n')
            elif valor_saque == 0:
                print('\nINFELIZMENTE AINDA NÃO FOI LANÇADA A NOTA DE ZERO REAIS.\nSUA ANTA!\n')
            else:
                conta1.sacar(valor_saque)
                print('SAQUE DE R$ {} REALZIADO.'.format(valor_saque))
                print('##################################################\n')
    
    def realizar_deposito():
        print('##################################################')
        try:
            valor_deposito = float(input('Digite o valor a ser DEPOSITADO: '))
        except:
            print('FAVOR DIGITAR UM VALOR!')
        else:
            conta1.depositar(valor_deposito)
            print('DEPOSITO DE R$ {} REALZIADO NA CONTA DE {}.'.format(valor_deposito, conta1.titular))
            print('##################################################\n')

    def alterar_limite_saque():
        print('##################################################')
        novo_limite = float(input('Informe o NOVO limite de saque: '))
        conta1.alterar_limite(novo_limite)
        print('O NOVO LIMITE DE {} É DE R$ {}'.format(conta1.titular, conta1.limite_saque))
        print('##################################################\n')

    # EXECUTA O MENU
    menu()

main()