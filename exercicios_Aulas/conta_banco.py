class conta_banco:
    def __init__(self, banco, agencia, conta, titular, tipo, saldo, limite_saque):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.titular = titular
        self.tipo = tipo
        self.saldo = saldo
        self.limite_saque = limite_saque

    def sacar(self, valor):
        self.saldo -= valor
    
    def depositar(self, valor):
        self.saldo += valor

    def imprimi_dados(self):
        print('\n#######################')
        print('Dados da Conta\nBanco: {}\nAgencia: {}\nConta: {}\nTitular: {}\nTipo de Conta: {}\nSaldo: {}'.format(self.banco, self.agencia, self.conta, self.titular, self.tipo, self.saldo))
        print('#######################\n')

def main():
    banco = input('Informe o NOME do banco: ')
    agencia = input('Informe a AGENCIA: ')
    conta = input('Informe a CONTA do banco: ')
    titular = input('Informe o NOME do TITULAR: ')
    tipo = input('Informe o TIPO da conta(Poupança ou Corrente): ')
    limite_salque = float(input('Informe o LIMITE DE SAQUE para essa conta: '))

    conta1 = conta_banco(banco, agencia, conta, titular, tipo, 0, limite_salque)
    print('DADOS INICIAS DA CONTA')
    conta1.imprimi_dados()
    
    print('##################################################')
    deposito = float(input('Digite o valor a ser DEPOSITADO: '))
    conta1.depositar(deposito)
    print('A conta {} de {} tem agora R$ {}'.format(conta1.tipo, conta1.titular, conta1.saldo))
    print('##################################################\n')

    print('##################################################')
    saque = float(input('Digite o valor a ser SACADO: '))
    conta1.sacar(saque)
    print('A conta {} de {} tem agora R$ {}'.format(conta1.tipo, conta1.titular, conta1.saldo))
    print('##################################################\n')

    conta1.imprimi_dados()

main()