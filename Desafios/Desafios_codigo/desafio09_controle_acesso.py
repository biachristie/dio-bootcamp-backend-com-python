# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",
}

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

# TODO: Verifique se o usuário existe e a senha está correta:


def verificar_permissao():
    for chave, valor in usuarios.items():
        if chave == usuario and valor == senha:
            print("Acesso permitido")
            return

    print("Usuário ou senha incorretos")


verificar_permissao()
