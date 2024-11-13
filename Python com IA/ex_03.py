compras_clientes = {
    "Pedro": ["pão", "arroz", "leite", "maçã"],
    "Ana":["leite", "pão", "maçã"],
    "Maria":["maçã", "leite"]
}
quantidade = len(compras_clientes["Pedro"])
quantidade2 = len(compras_clientes["Ana"])
quantidade1 = len(compras_clientes["Maria"])
total = quantidade,quantidade1,quantidade2
for i,o in compras_clientes.items():

    print(i,len(o))




