# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:

def definir_prioridade(paciente):
    nome, idade, status = paciente

    if status == "urgente":
        prioridade = 1
    elif idade > 60:
        prioridade = 2
    else:
        prioridade = 3

    return (prioridade, -idade)

ordem_atendimento = sorted(pacientes, key=definir_prioridade)

# TODO: Exiba a ordem de atendimento com título e vírgulas:

nomes_atendimento = ", ".join([paciente[0] for paciente in ordem_atendimento])

print(f"Ordem de Atendimento: {nomes_atendimento}")