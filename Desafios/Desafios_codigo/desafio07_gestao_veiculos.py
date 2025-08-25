from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:

    def verificar_antiguidade(veiculo):
        ano_veiculo = veiculo.ano
        ano_atual = datetime.now().year
        
        diferenca = ano_atual - int(ano_veiculo)
        
        if diferenca > 20:
            return "Veículo antigo"
        
        return "Veículo novo"

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())