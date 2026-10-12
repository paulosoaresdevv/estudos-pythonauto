# Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada:

# "carro" → "Veículo terrestre"

# "bicicleta" → "Transporte sustentável"

# "avião" ou "helicóptero" → "Transporte aéreo"

# Qualquer outro → "Transporte desconhecido"

meio_de_transporte = str (input ("Digite um meio de transporte: "))
match meio_de_transporte:
  case "carro":
    print ("Veículo terrestre")
  case "bicicleta":
    print ("Transporte sustentável")
  case "avião" | "helicóptero":
    print ("Tansporte áereo")
  case _:
    print ("Transporte desconhecido.")