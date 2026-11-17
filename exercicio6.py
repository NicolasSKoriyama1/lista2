livros = [
    [1, "Dom Casmurro", "Machado de Assis", 2024],
    [2, "1984", "George Orwell", 1949],
    [3, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943]
]


titulo_procurado = "1984"


for livro in livros:
    if livro[1] == titulo_procurado:
        print("Livro localizado!")
        break
