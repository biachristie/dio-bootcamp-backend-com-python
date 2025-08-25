from abc import ABC, abstractmethod
from datetime import datetime
import textwrap


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def cpf(self):
        return self._cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(self, cliente, numero):
        return self(numero, cliente)

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação inválida! Não há saldo suficiente.")
        
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True

        else:
            print("\nOperação inválida! O valor informado é inválido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
            return True
        
        else:
            print("\nOperação inválida! O valor informado é inválido.")
        
        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques > self._limite_saques

        if excedeu_limite:
            print("\nOperação inválida! O valor é maior que o limite diário.")

        elif excedeu_saques:
            print("\nOperação inválida! Número máximo diário de saques atingido.")
        
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def imprimir_menu():
    menu = """
    ================= MENU ==================

    [u] Criar cliente
    [c] Criar conta corrente
    [l] Listar contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    return input(textwrap.dedent(menu))


def main():
    clientes = []
    contas = []

    while True:
        opcao = imprimir_menu()

        if opcao == "u":
            criar_cliente(clientes)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta , clientes, contas)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            emitir_extrato(clientes)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]

    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta cadastrada!")
        return
    
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("\nInforme o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("\nInforme o valor do depósito: "))

    if valor > 0:
        transacao = Deposito(valor)
        conta = recuperar_conta_cliente(cliente)

        if not conta:
            return

        cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("\nInforme o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    valor = float(input("\nInforme o valor do saque: "))
    
    if valor > 0:
        transacao = Saque(valor)
        conta = recuperar_conta_cliente(cliente)

        if not conta:
            return
    
        cliente.realizar_transacao(conta, transacao)


def emitir_extrato(clientes):
    cpf = input("\nInforme o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    print("\n=============== EXTRATO =================")
    extrato = ""
    transacoes = conta.historico.transacoes

    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao["tipo"]}:  R$ {transacao["valor"]:.2f}"

    print(extrato)
    print(f"\nSaldo: \tR$ {conta.saldo:.2f}")
    print("\n=========================================")


def criar_cliente(clientes):
    cpf = input("\nInforme o CPF do usuário: ")
    
    if not (cpf.isdigit() and len(cpf) == 11):
        print("Operação inválida! CPF deve conter 11 dígitos numéricos.")
        return
    
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Operação inválida! Usuário já cadastrado no sistema.")
        return
    
    nome = input("\nInforme o nome do usuário: ")
    data_nascimento = input("\nInforme a data de nascimento do usuário (dd-mm-aaaa): ")
    endereco = input("\nInforme o endereço do usuário (Logradouro, número - Bairro - Cidade/Sigla do Estado): ")
    
    if not validar_endereco(endereco):
        print("Operação inválida! Endereço deve seguir o padrão.")
        return

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!")


def validar_endereco(endereco):
    partes = endereco.split(" - ")

    if len(partes) != 3:
        return False
    
    logradouro_numero = partes[0].split(", ")
    cidade_estado = partes[2].split("/")

    if len(logradouro_numero) != 2 or len(cidade_estado) != 2:
        return False
    
    numero = logradouro_numero[1]
    sigla_estado = cidade_estado[1]

    if not (any(caracter.isdigit() for caracter in numero)):
        return False
    
    if not (len(sigla_estado) == 2 and sigla_estado.isupper() and sigla_estado.isalpha()):
        return False

    return True


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado! Fluxo de criação de conta encerrado.")
        return

    nova_conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(nova_conta)
    cliente.adicionar_conta(nova_conta)

    print("\nConta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print("=" * 41)
        print(textwrap.dedent(str(conta)))


main()