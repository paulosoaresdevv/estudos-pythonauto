# Exercício 2 – Pegando um trecho da frase
# Peça ao usuário uma frase e dois números: início e fim. Mostre o fatiamento da frase entre esses índices.

frase = input("Digite uma frase: ")
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
# print(frase[num1:num2])
print(f"A frase fatiada é: {frase[num1:num2]}")