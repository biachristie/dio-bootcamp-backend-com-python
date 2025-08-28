# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# Entrada do usuário
produto = input().strip()

# TODO: Verifique se o produto está no estoque:


def verificar_estoque():
    status = "Produto disponível" if produto in estoque else "Produto esgotado"
    print(status)


verificar_estoque()
