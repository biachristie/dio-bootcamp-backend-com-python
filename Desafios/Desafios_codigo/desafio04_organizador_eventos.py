# Dicionário para agrupar participantes por tema
from collections import defaultdict


eventos = defaultdict(list)

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:

for _ in range(n):
    dado = input().split(", ")
    
    eventos[dado[1]].append(dado[0])

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")