# Crie um menu com 3 opções:

# 1. Pizza

# 2. Sushi

# 3. Salada

# O usuário digita um número. O programa mostra o prato escolhido. Se digitar qualquer outro número, exiba: "Opção inválida."

menu = int (input ("Digite o númnero do seu prato (1 a 3): "))

match menu:
  case 1:
    print ("Pizza")
  case 2:
    print ("Sushi")
  case 3:
    print ("Salada")
  case _:
    print ("Opção inválida.")