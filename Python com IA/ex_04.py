notas_alunos = {
    "Ana": [8.5, 9.0, 7.5],
    "Pedro": [5.5, 6.0, 7.0],
    "Maria": [7.0, 7.5, 6.0]
}

print('Digite o Nome do aluno que Deseja Saber a nota')
for i in notas_alunos:
    for o in i:
        if o > 7:
            print('Aluno foi aprovado')
    else:
        print('Aluno foi reprovado')

