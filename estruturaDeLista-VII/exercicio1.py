"""

Como sugestão de prática, indicamos você a criar um novo script python seguindo as orientações a seguir:

Crie uma lista abaixo com a seguinte palavra:
“PYTHON”

A lista deve conter as letras separadas e em maiúsculas.
Crie uma nova lista somente com as três últimas letras da palavra “PYTHON”.


"""

lista = ["P", "Y" , "T", "H", "O", "N"]

for i in range(len(lista)):
    print(lista[i])

nova_list = lista[3:6]
print(nova_list)