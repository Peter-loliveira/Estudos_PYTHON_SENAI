class ContaBanco:
    _id = 0

    @property
    def id(cls):
        return cls._id

    @classmethod
    def nova_id_conta(cls, ultima_conta):
        cls._id = ultima_conta + 1

    def __init__(self, titular, tipo_Conta, tipos_permitidos):
        # ContaBanco.nova_id_conta(self.id)
        self.titular = titular
        self.tipo_Conta = ''
        self._saldo = 0
        self._limite_saque = 1000.00
        self._num_conta = ' '

        print('Conta Nova')
        print("Dados Conta:")
        print(self.saldo)
        # saldo(500)
        print(self.saldo)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novoSaldo):
        self._saldo = novoSaldo

    @property
    def tipo_Conta(self):
        return self._tipo_Conta

    @tipo_Conta.setter
    def tipo_Conta(self, TipoConta):
        tiposPermitidos = ['c', 'p']
        if tiposPermitidos not in TipoConta:
            self._tipo_Conta = tiposPermitidos[-1]
        else:
            self._tipo_Conta = tiposPermitidos

    def saque(self, valor):
        if valor > (self._saldo):
            print('Saldo Insulficiente')
        elif valor > self._limite_saque:
            print(" valor de saque acima do valor permitido.")
        else:
            self._saldo -= valor
            print(" Saque realizado com sucesso, Aguarde a contagem das notas!")

    def deposito(self, valor):
        if valor > 0:
            self._saldo += valor
            print(" Deposito realizado com sucesso!!")

        @property
        def limite_saque(self):
            return self._limite_saque

        @limite_saque.setter
        def limite_saque(self, novo_limite):
            self._limite_saque = novo_limite

        def exibe(self):
            print('Numero da conta:', self.id, '| Titular:', self.titular, '| Tipo Conta:', self._tipo_conta)
            print('Limite de Saque: ', self.limite_saque)
            print('Saldo:', self.saldo)
            print('\n')
