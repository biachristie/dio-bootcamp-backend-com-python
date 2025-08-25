class Pedido:
    def __init__(self):
        self.itens = []  
    
    
    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:

    def adicionar_item(self, novo_preco):
        # TODO: Adicione o preço do item à lista:

        self.itens.append(novo_preco)


    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:

    def calcular_total(self):
        soma = 0

        # TODO: Retorne a soma de todos os preços

        for preco in self.itens:
            soma += preco
        
        return soma


quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    #TODO: Chame o método adicionar_item corretamente: 

    pedido.adicionar_item(float(preco))

# TODO: Exiba o total formatado com duas casas decimais:

preco_total = pedido.calcular_total()

print(f"{preco_total:.2f}")