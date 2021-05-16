import random
import webbrowser

name = input("Digite su nombre por favor: ")

while True:
    choices = ["piedra","papel","tijeras"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("\n¿piedra, papel o tijeras?: ").lower()

    if player == computer:
        print("Maquina: ", computer)
        print("{}: {}".format(name, player))
        print("Empate!")

    elif player == "piedra":
        if computer == "papel":
            print("Maquina: ", computer)
            print("{}: {}".format(name, player))
            print("Perdiste!")
        if computer == "tijeras":
            print("Maquina: ", computer)
            print("{}: {}".format(name, player))
            print("Ganaste!")

    elif player == "tijeras":
        if computer == "piedra":
            print("Maquina: ", computer)
            print("{}: {}".format(name, player))
            print("Perdiste!")
        if computer == "papel":
            print("Maquina: ", computer)
            print("{}: {}".format(name, player))
            print("Ganaste!")

    elif player == "papel":
        if computer == "tijeras":
            print("Maquina: ", computer)
            print("{}: {}".format(name, player))
            print("Perdiste!")
        if computer == "piedra":
            print("Maquina: ", computer)
            print("{}: {}".format(name, player))
            print("Ganaste!")

    play_again = input("\n¿Quiere jugar de nuevo? (s/n): ").lower()

    if play_again != "s":
        break

page = input("\nEste programa fue creado usando Python, ¿Desea ver el codigo fuente de este juego? (s/n): ").lower()

if page == "s":
	webbrowser.open_new_tab("https://github.com/Arturo-sh/rock_paper_scissors_game/blob/main/rock_paper_scissors_game.py")
	print("\nGracias por usar este sotfware :)")
else:
	print("\nGracias por usar este sotfware :)")
	input('Presione Enter para continuar....')
