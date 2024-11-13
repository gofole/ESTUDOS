estudantes = {
    "Ana": ["Matemática", "História"],
    "Pedro": ["Biologia", "Física"],
    "Maria": ["Química", "Matemática"]
}

estudantes["Ana"]=['Biologia','Historia']
estudantes['Maria']=['Matematica']
for i,o in estudantes.items():
    print(i,o)