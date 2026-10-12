# Crie um código onde é solicitado para o usuário inserir dois valores: o ano atual, e o ano de nascimento. O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console.



ano = int (input ("Digite em que estamos: "))
nascimento = int (input("Digite o ano em que você nasceu: "))
resultado = ano - nascimento
print (f"Se estamos em {ano} e voce nasceu em {nascimento}, voce tem {resultado} anos")