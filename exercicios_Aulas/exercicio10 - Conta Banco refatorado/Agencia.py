class Agencia:
    def __init__(self, numero):
        self.numero = numero
        self._lista_contas = []

    def criar_conta(self,conta):
        if conta not in self._lista_contas:
            self._lista_contas.append(conta)

    def listar_contas(self):
        for conta in self._lista_contas:
            print( 'Conta Nr.: ', conta.num_conta, '| Tutular:', conta.titular.nome, '| Tipo da Conta:', conta.tipo_conta, ' | Saldo: R$', format(conta.saldo,'.2f'))