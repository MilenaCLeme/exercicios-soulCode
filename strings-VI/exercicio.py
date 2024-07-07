"""

Como sugestão de prática, indicamos você a criar um novo script python seguindo as orientações a seguir:

Crie uma string contendo o alfabeto com letras maiúsculas separado por espaços.
Percorra e imprima essa string com enumerate.
Substitua os espaços por traço. “-” e imprima para o usuário.


"""

alfabeto = "A B C D E F J H I J K L M N O P Q R S T U V W X Y Z"

for k, v in enumerate(alfabeto):
    print(k, v)

print(alfabeto.replace(" ", "-"))