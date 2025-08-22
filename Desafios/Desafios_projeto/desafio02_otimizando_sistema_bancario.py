import textwrap


def imprimir_menu():
    menu = """
    ================= MENU ==================

    [u] Criar usuário
    [c] Criar conta corrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    return input(textwrap.dedent(menu))


def emitir_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato, True

    print("Operação falhou! O valor informado é inválido.")        
    return saldo, extrato, False


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques, True

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques, False


def criar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("\nInforme a data de nascimento do usuário: ")
    
    cpf = input("\nInforme o CPF do usuário: ")
    
    if not (cpf.isdigit() and len(cpf) == 11):
        print("Operação inválida! CPF deve conter 11 dígitos numéricos.")
        return None

    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Operação inválida! Usuário já cadastrado no sistema.")
        return None
    
    endereco = input("\nInforme o endereço do usuário (Logradouro, número - Bairro - Cidade/Sigla do Estado): ")
    
    if not validar_endereco(endereco):
        print("Operação inválida! Endereço deve seguir o padrão.")
        return None

    return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}


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


def criar_conta_corrente(agencia, numero, usuarios):
    usuario_encontrado = None

    cpf = input("Informe o CPF do usuário cadastrado: ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        return {"agencia": agencia, "numero_conta": numero, "usuario": usuario_encontrado}
    else:
        print("\nOperação inválida! Usuário não cadastrado no sistema.")
        return None


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = imprimir_menu()

        if opcao == "u":
            novo_usuario = criar_usuario(usuarios)

            if novo_usuario:
                usuarios.append(novo_usuario)
                print("\nUsuário cadastrado com sucesso!")

        elif opcao == "c":
            numero_conta = len(contas) + 1
            nova_conta = criar_conta_corrente(AGENCIA, numero_conta , usuarios)

            if nova_conta:
                contas.append(nova_conta)
                print("\nConta corrente cadastrada com sucesso!")

        elif opcao == "d":
            valor_deposito = float(input("Informe o valor do depósito: "))

            saldo, extrato, sucesso = depositar(saldo, valor_deposito, extrato)

            if sucesso:
                print("\nDepósito realizado com sucesso!")

        elif opcao == "s":
            valor_saque = float(input("Informe o valor do saque: "))
            
            saldo, extrato, numero_saques, sucesso = sacar(
                saldo=saldo, 
                valor=valor_saque, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES
            )

            if sucesso:
                print("\nSaque realizado com sucesso!")

        elif opcao == "e":
            emitir_extrato(extrato, saldo=saldo)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()