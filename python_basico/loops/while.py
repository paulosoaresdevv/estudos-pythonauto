# while: repete o bloco enquanto a condição for verdadeira.
# Se a condição nunca ficar falsa, vira um loop infinito.

contador = 1
while contador <= 5:
  print("Contador: %d" % contador)
  contador+=1

senha = ''
while senha != "python":
  senha = input("Digite sua senha: ")
print("Senha correta!")
