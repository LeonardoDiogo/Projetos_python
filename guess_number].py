
import random

print("seja muito bem vindo ao guess number")
choice_number = input("digite o numero teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("erro: valor informado nao é numerico. favor execute novamente e informe um numero")
    quit()

random_number = random.randint(0, choice_number)

n_choice = 0


while True:
    answer_user = input("adivinhe o numero: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado nao é numerico. Favor infome o numero!")
        continue

    n_choice = n_choice + 1

    if answer_user == random_number:
        print("acertou")
        break
    elif answer_user > random_number:
        print("chutou alto, o numero randomico é menor que isso..")
    else:
        print("chutou baixo, o numero randomico é maior que isso..")
print("Nº de tentativas: " + str(n_choice))
