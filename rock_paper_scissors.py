import random

user_point = 0
computer_points = 0

options = ["R", "T", "P"]

while True:
    user_choice = input(
        "Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair").lower()

    if user_choice == "q":
        break

    computer_choice = random.randint(0, 2)


print("Tchau Tchau")
