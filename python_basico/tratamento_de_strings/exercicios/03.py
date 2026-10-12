# Exercício 3 – Detectando palavras proibidas
# Peça ao usuário para escrever uma mensagem. Verifique se ela contém a palavra "bomba", e imprima um alerta se sim.

frase = input("Digite uma frase: ")
if 'bomba'.lower() in frase.lower():
  print("ALERTA! Essa frase tem a palavra bomba")
else:
  print("Nada de bomba!")