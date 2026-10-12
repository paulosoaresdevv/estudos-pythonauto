pessoa = {
  "nome": "Júlio",
  "idade": 25,
  "cidade": 'São Paulo',
  "profissoes": ['Programador', 'Designer', 'Pintor']
}

#puxar um unico item do dicionario:
# print(pessoa['idade'])

#alterar um item do dicionario:
# pessoa['idade'] = 26
# print(pessoa['idade'])

#deleter um item do dicionario:
# del pessoa['cidade']
# print(pessoa)

#mostrar todas as categorias de itens do dicionario:
# print(pessoa.keys())

#mostrar todos os valores de dentro das categorias de itens do dicionario:
# print(pessoa.values())

# mostrar um valor especifico de dentro do dicionario
# valores = list(pessoa.values())
# print(valores[2])

#mostrar todos as categorias e valores de dentro de um dicionario
# print(pessoa.items())

# mostrar uma mensagem para informação não existente ao inves de erro
# print(pessoa.get('telefome', 'Não existe'))

# remover uma categoria especifica do dicionario e mostrar o item
# item_removido = pessoa.pop('profissoes')
# print(f"Item removido:{item_removido}")
# print(pessoa)

#exemplo de uso:

# produto = {
#   "nome": "Notebook",
#   "preco": 3500,
#   "estoque": 12
# }

# print(f"Ainda restam {produto['estoque']} unidades do produto {produto['nome']}")