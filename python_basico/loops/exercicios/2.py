# Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

total = 0
for i in range (5):
  num = int(input("Digite um número: "))
  total = i+num
print(total)

## revisar depois, demorei para entender e so cheguei ao resultado com a ajuda do claude, sem dar a resposta, mas me ajudando a chegar nela.

#correção do professor:
# numeros = []
# for n in range (1,6):
#   numero = int(input("Digite um número: "))
#   numeros.append(numero)
# resultado = 0
# for numero in numeros:
#   resultado += numero
# print (f"o resultado é: {resultado}")