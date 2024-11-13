contatos = {
    "Ana": "1234-5678",
    "Pedro": "8765-4321",
    "Maria": "1357-2468"
}
print("Voce Deseja Adiconar Mais um contado se sim digite a baixo O numero De telefone,nome e Numero de celular")
contatos[input('Digite O Nome da Pessoa')]=int(input('Digite o Numero da pessoa'))
for i,o in contatos.items():
    print(i,o)

print(contatos[input('Digite O nome do contato que Deseja ver o Numero')])