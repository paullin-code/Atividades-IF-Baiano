class ContaBancaria():
    def __init__(self, titular, saldo, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta

    def depositar(self):
        valor = float(input("Digite o valor a ser depositado: "))
        self.saldo += valor
        print(f"O saldo da conta do(a) {self.titular} é de R$ {self.saldo}")
    
    def sacar(self):
        valor = float(input("Digite o valor a ser sacado: "))
        self.saldo -= valor
        print(f"O saldo da conta atual do(a) {self.titular} é de R$ {self.saldo} e ele acabou de sacar R$ {valor}")
    
    def transferir(self, saldo_da_conta):
        valor = float(input("Digite o valor a ser transferido: "))
        if self.saldo >= valor:
            self.saldo -= valor
            saldo_da_conta += valor
            return saldo_da_conta
        else:
            print("Saldo insuficiente!")

    def verificar_saldo(self):
        print(f"O saldo da conta do(a) {self.titular} é de R$ {self.saldo}")

titular = input("Digite o nome do titular da conta: ")
saldo = float(input("Digite o saldo da conta: "))
numero_conta = input("Digite o número da conta: ")
tipo_conta = (input("Digite o tipo da conta (Corrente/Poupança): "))

conta2 = ContaBancaria("Jao", 3000, "109", "Corrente")


conta = ContaBancaria(titular, saldo, numero_conta, tipo_conta)
conta.depositar()
conta.sacar()
conta2.saldo = conta.transferir(conta2.saldo)
conta.verificar_saldo()
conta2.verificar_saldo()