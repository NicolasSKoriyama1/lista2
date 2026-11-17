funcionarios = [
    [1, "Ana Silva", "Analista de Sistemas", 5500.00],
    [2, "Carlos Souza", "Gerente de Projetos", 8200.50]
]

# Desempacotando os itens dentro do enumerate para evitar colchetes extras
for indice, (id_func, nome, cargo, salario) in enumerate(funcionarios):
    if id_func == 2:
        novo_salario = salario + 500
        funcionarios[indice][3] = novo_salario
        print(f"Aumento aplicado! Novo salário de {nome}: R$ {novo_salario:.2f}")
        break

# Conferindo a lista atualizada
print(funcionarios)
