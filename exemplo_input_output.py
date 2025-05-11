# Exemplo simples de input e output em Python

# Pedindo o nome do usuário
nome = input("Digite seu nome: ")

# Pedindo a idade do usuário
idade = input("Digite sua idade: ")

# Pedindo a cidade onde mora
cidade = input("Digite a cidade onde você mora: ")

# Mostrando as informações coletadas
print("\n=== Informações Coletadas ===")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")

# Exemplo de cálculo simples com a idade
idade_futura = int(idade) + 5
print(f"\nEm 5 anos você terá {idade_futura} anos")

# Mensagem personalizada
print(f"\nOlá {nome}! É um prazer te conhecer!")
print(f"Que legal que você mora em {cidade}!") 