import random

def validacion():
    decision = ''
    while decision not in ('y', 'n'):
        decision = input(f"Escribe (y) para jugar y (n) para salir ").lower()
    return decision

def round_header(round_num):
    print("*" * 19)
    print(" " * 6 + f"ROUND {round_num}" + " " * 6)
    print("*" * 19 + "\n")

def marcador(user_wins, computer_wins):
    return {
        "User wins" : user_wins,
        "Computer wins" : computer_wins
    }



round_num = 1

computer_wins = 0
user_wins = 0

options = ("piedra", "papel", "tijera")

while True:
    eleccion_usuario = validacion()
    if eleccion_usuario == 'n':
        print("Gracias por jugar con nosotros")
        break
    round_header(round_num)
    marcador(user_wins, computer_wins)

    round_num += 1

    user_choise = input("Elije piedra, papel o tijera -> ").lower()

    if user_choise not in options:
        print(f"La opción {user_choise} no es valida")
        continue

    computer_choise = random.choice(options)
    print(f"La computadora eligió -> {computer_choise} \n")

    if user_choise == computer_choise:
        print("EMPATE")
        continue
    
    if user_choise == "piedra":
        if computer_choise == "tijera":
            print("USER WINS!!")
            user_wins += 1
        else:
            print("COMPUTER WINS!!")
            computer_wins += 1
    
    if user_choise == "papel":
        if computer_choise == "piedra":
            print("USER WINS!!")
            user_wins += 1
        else:
            print("COMPUTER WINS!!")
            computer_wins += 1
    
    if user_choise == "tijera":
        if computer_choise == "papel":
            print("USER WINS!!")
            user_wins += 1
        else:
            print("COMPUTER WINS!!")
            computer_wins += 1