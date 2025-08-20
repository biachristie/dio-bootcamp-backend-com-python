titulo_menu = "Menu"

menu = f"""
{titulo_menu.center(30, "-")}

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        if valor > 0:
            
            if numero_saques < LIMITE_SAQUES:

                if valor <= saldo:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor:.2f}\n"
                
                else:
                    print("Operação falhou! Não há saldo suficiente.")

            else:
                print("Operação falhou! Número de saques maior do que o limite diário.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        titulo_extrato = "Extrato"

        print(f"""{titulo_extrato.center(30, "-")}\n""")

        if not extrato:
            print("Não houve movimentações.\n")

        else:
            print(extrato)
        
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Obrigada por usar nosso sistema. Volte sempre!\n")
        break

    else:
        print("Operação inválida! Selecione novamente a opção desejada.")