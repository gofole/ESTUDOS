# meu_dicionario ={
#     'nome': 'ana',
#     'idade':  30,
#     'cidade':  'sao paulo'
# }
# meu_dicionario['Profissao']='Dentista'
# meu_dicionario['cidade']='belo horizonte'
# del meu_dicionario['idade']
# print(meu_dicionario)


# frutas={
#     'maça':5,
#     'banana':3,
#     'laranja':4
#     }
# for chave,valor in frutas.items():
#     print(f' a fruta é {chave} e a quantidade de cada fruta é {valor}')


# pessoas = {
#     'nome':'ana',
#     'idade':25,
#     'cidade':'Sao  paulo'
#     }
# for i in pessoas.values():
#     print(i) 


# contato = {
#     'telefone':123456789,
#     'Email':'contato@exemplo.com'

# }
# contato['telefone']=987654321
# print(contato)


# aluno = {
#     'nome':'joao',
#     'nota':7.5
# }
# aluno['curso']='Matematica'
# print(aluno)


# produto={
#     'nome':'Laptop',
#     'preço':3500,
#     'Quantidade':10
# }
# del produto['Quantidade']
# print(produto)


# biblioteca = {
#     "1984": {"autor": "George Orwell", "ano": 1949},
#     "O Senhor dos Anéis": {"autor": "J.R.R. Tolkien", "ano": 1954},
#     "O Hobbit": {"autor": "J.R.R. Tolkien", "ano": 1937}
# }

# biblioteca['games of Thrones']='Autor:George R. R. Martin,'' ano : 1996'

# for i,o in biblioteca.items():
#     print(i,o)


# estudantes = {
#     "Ana": ["Matemática", "História"],
#     "Pedro": ["Biologia", "Física"],
#     "Maria": ["Química", "Matemática"]
# }

# estudantes["Ana"]=['Biologia','Historia']
# estudantes['Maria']=['Matematica']
# for i,o in estudantes.items():
#     print(i,o)


# compras_clientes = {
#     "Pedro": ["pão", "arroz", "leite", "maçã"],
#     "Ana":["leite", "pão", "maçã"],
#     "Maria":["maçã", "leite"]
# }
# for i,o in compras_clientes.items():

#     print(i,len(o))



# notas_alunos = {
#     "Ana": [8.5, 9.0, 7.5],
#     "Pedro": [5.5, 6.0, 7.0],
#     "Maria": [7.0, 7.5, 6.0]
# }

# print('Digite o Nome do aluno que Deseja Saber a nota')
# for i in notas_alunos:
#     for o in i:
#         if o > 7:
#             print('Aluno foi aprovado')
#     else:
#         print('Aluno foi reprovado')

# contatos = {
#     "Ana": "1234-5678",
#     "Pedro": "8765-4321",
#     "Maria": "1357-2468"
# }
# print("Voce Deseja Adiconar Mais um contado se sim digite a baixo O numero De telefone,nome e Numero de celular")
# contatos[input('Digite O Nome da Pessoa')]=int(input('Digite o Numero da pessoa'))
# for i,o in contatos.items():
#     print(i,o)

# print(contatos[input('Digite O nome do contato que Deseja ver o Numero')])



# frutas_cores ={
#     'morando':'vermelho',
#     'banana':'Amarelo',
#     'Uva':'roxo'
# }
# for i,o in frutas_cores.items():
#     print(i,)




# produtos={
#     'maça':2,
#     'banana':1.5,
#     'laranja':3
# }
# for i in produtos.values():
#     print(i)




# idades={
#     'Alice':30,
#     'bob':25,
#     'carol':22
# }
# for i,o in idades.items():
#     print(f'nome {i} sua Idade é {o}')


# contagem={
#     'a':3,
#     'b':5,
#     'c':2
# }
# for i,o in contagem.items():
#     print(f' o valor de {i} é {o+o}')


# notas={
#     'ana':8,
#     'pedro':5,
#     'Luiza':9,
#     'Joao':4

# }
# super_alunos={

# }
# for i,o in notas.items():
#     if o >=7:
#         super_alunos[i]=o

# print(super_alunos,'sao os Super Alunos')

# estoque ={
#     'canetas':10,
#     'cadernos':5,
#     'borrachas':20
# }
# estoque['cadernos']=8

# estoque['Lapis']=15
# for i,o in estoque.items():
#     print(i,o)

frutas={
    'maça':5,
    'banana':3,
    'laranja':0
}
del frutas['banana','maça','laranja']
print(frutas)





