# for: repete o bloco uma vez para cada elemento de uma sequência.
# A variável do laço recebe o próximo elemento a cada volta.

# for numero in range (1,6):
#   print("Contando: %d" % numero)

# frutas = ['maça', 'banana', 'uva', 'pêssego']
# for frutas in frutas:
#   print("Fruta atual: %s" % frutas)

#-------------------------------------------

#tabuada do 1 ao 10:
# for multiplicador in range (1,11):
#   for multiplicado in range (1,11):
#     print(f"{multiplicado} x {multiplicador} = {multiplicado*multiplicador}")

#-------------------------------------------

#loop para verificar e encontrar um nome em uma lista
# pessoas = ['ana', 'matheus', 'marcos', 'julia', 'fernanda']
# for nomes in pessoas:
#   print("Verificando: %s" % nomes)
#   if nomes == 'julia':
#     print("Nome encontrado: %s" % nomes)
#     break #serve para quebrar um loop ao achar o que busca.
# print("Busca encerrada!")

# codigo para verificar numeros pares:
# for numero in range (1,11):
#   if numero % 2 == 0:
#     continue #serve para descartar um caso sem quebrar um loop
#   print ("Número: %d" % numero)