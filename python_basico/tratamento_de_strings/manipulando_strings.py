#pegar uma letra especifica de uma variavel de string.
'''
fruta = "Melancia"
print(fruta[0])
fruta = "Melancia"
print(fruta[0:2])
fruta = "Melancia"
print(fruta[-2])
'''

frase = "eu amo python"

#pegar quantos index tem em uma variavel de strings
'''
print(len(frase))

rase_tam = len(frase)
print(frase_tam)
'''

#contar quantas vezes um caractere aparece em uma variavel de string
'''
contagem = frase.count('o')
print(contagem)
'''

#procurar onde esta determinado caractere
'''
print(frase.find('m'))
'''

# verificar se uma determinada frase ou caractere esta em uma variavel string
'''
if 'python' in frase:
  print("python está na frase.")
else:
  print("python não está na frase.")
'''

#deixar frase toda em minusculo
# print(frase.lower())

#deixar frase toda em maisculo
# print(frase.upper())

#deixa primeira letra em maisculo
# print(frase.capitalize())

#deixa primeira letra de cada palavra em maisculo
# print(frase.title())

#remover espaços das laterais
# print(frase.strip())

#substituir caracteres
# print(frase.replace('o', 'x'))

