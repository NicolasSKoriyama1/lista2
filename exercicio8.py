livros = [
    [1, "Dom Casmurro", "Machado de Assis", 2024],
    [2, "1984", "George Orwell", 1949],
    [3, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943]
]


id_remover = 2


for indice, livro in enumerate(livros):
    if livro == id_remover:
        livros.pop(indice)
        break 


print(livros)
