# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.

credenciais_corretas = {
  "usuario": "phhsoares",
  "senha": "1234phsc"
}

#forma de fiz:
'''
usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")
credenciais_usuario = {
  "usuario": usuario,
  "senha": senha
}
'''

#forma mais simples:
credenciais_usuario = {
  "usuario": input("Digite seu usuario: "),
  "senha": input("Digite sua senha: ")
}
if credenciais_corretas == credenciais_usuario:
  print("Login bem-sucedido!")
else:
  print("Usuário ou senha incorretos!")