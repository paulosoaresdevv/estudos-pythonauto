# Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).
# Quando o usuário digitar 0, o programa para e mostra o total economizado.

cofrinho = 0
num = 1
while num != 0:
  num = float(input("Qual o valor guardado: "))
  cofrinho = cofrinho + num
print("O total economizado foi: %.2f" % cofrinho)

# anteriomente eu cheguei nessa resposta:

# cofrinho = 0
# while cofrinho >= 0:
#   num = float(input("Qual o valor guardado: "))
#   cofrinho = cofrinho + num
#   if num == 0:
#     print("O total economizado foi: %f" % cofrinho)

# ela continua pedindo mesmo depois do 0, joguei no claude para ele conferir e me ajudar a resolver e cheguei na resposta acima, retirando o if e colocando um valor inicial para o num iniciar a rodada.

#correção do professor:
total = 0
while True:
  valor = float(input("Insira algo no cofrinho: "))
  if valor == 0:
    break
  total += valor
print(f"O valor total guardado é: ")