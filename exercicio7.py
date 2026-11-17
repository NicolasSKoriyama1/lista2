livros = [
    [1, "Dom Casmurro", "Machado de Assis", 2024],
    [2, "1984", "George Orwell", 1949],
    [3, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943]
]

id_procurado = 99
encontrado = False  


for livro in livros:
    if livro[0] == id_procurado:
        print(f"Livro localizado: {livro[1]}")
        encontrado = True
        break


if not encontrado:
    print("Livro não encontrado")
