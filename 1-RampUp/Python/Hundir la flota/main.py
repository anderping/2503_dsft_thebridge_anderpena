from board import Board, LETTER_COOR, NUM_COOR, INITIAL_BOARD
import time
import os
from playsound import playsound
import numpy as np
import vlc
import random


ORIENTATION_LIST = ["N", "S", "E", "W"]
SHIP_LIST = ["four_ship", "three_ship", "two_ship", "one_ship"]

SHOW_PC_SHIPS = True

VLC_COMMAND = [r"C:/Program Files/VideoLAN/VLC/vlc.exe",
               "--play-and-exit",
                r"C:/Users/defco/OneDrive/Escritorio/Cursos/Programación/Cursados/Data Science Bootcamp/2503_dsft_thebridge_anderpena/1-RampUp/Python/Hundir la flota/videos/canon.mp4"
                ]

TITLE = r"""
                   _        ______  _________ _______    _        _______    _______  _        _______ _________ _______ 
|\     /||\     /|( (    /|(  __  \ \__   __/(  ____ )  ( \      (  ___  )  (  ____ \( \      (  ___  )\__   __/(  ___  )
| )   ( || )   ( ||  \  ( || (  \  )   ) (   | (    )|  | (      | (   ) |  | (    \/| (      | (   ) |   ) (   | (   ) |
| (___) || |   | ||   \ | || |   ) |   | |   | (____)|  | |      | (___) |  | (__    | |      | |   | |   | |   | (___) |
|  ___  || |   | || (\ \) || |   | |   | |   |     __)  | |      |  ___  |  |  __)   | |      | |   | |   | |   |  ___  |
| (   ) || |   | || | \   || |   ) |   | |   | (\ (     | |      | (   ) |  | (      | |      | |   | |   | |   | (   ) |
| )   ( || (___) || )  \  || (__/  )___) (___| ) \ \__  | (____/\| )   ( |  | )      | (____/\| (___) |   | |   | )   ( |
|/     \|(_______)|/    )_)(______/ \_______/|/   \__/  (_______/|/     \|  |/       (_______/(_______)   )_(   |/     \|
                                                                                                                         
                                                    |    |    |                 
                                                    )_)  )_)  )_)              
                                                    )___))___))___)\            
                                                )____)____)_____)\\
                                                _____|____|____|____\\\__
                                        ---------\                   /---------
                                        ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
                                            ^^^^      ^^^^     ^^^    ^^
                                                ^^^^      ^^^

"""

ENHORABUENA = r"""
   __    __        ___  __    _      ___         __    __  _   
  /__\/\ \ \/\  /\/___\/__\  /_\    / __\/\ /\  /__\/\ \ \/_\  
 /_\ /  \/ / /_/ //  // \// //_\\  /__\// / \ \/_\ /  \/ //_\\ 
//__/ /\  / __  / \_// _  \/  _  \/ \/  \ \_/ //__/ /\  /  _  \
\__/\_\ \/\/ /_/\___/\/ \_/\_/ \_/\_____/\___/\__/\_\ \/\_/ \_/
                                                            
"""

COBARDE = r"""
 ________  ________  ________  ________  ________  ________  _______      
|\   ____\|\   __  \|\   __  \|\   __  \|\   __  \|\   ___ \|\  ___ \     
\ \  \___|\ \  \|\  \ \  \|\ /\ \  \|\  \ \  \|\  \ \  \_|\ \ \   __/|    
 \ \  \    \ \  \\\  \ \   __  \ \   __  \ \   _  _\ \  \ \\ \ \  \_|/__  
  \ \  \____\ \  \\\  \ \  \|\  \ \  \ \  \ \  \\  \\ \  \_\\ \ \  \_|\ \ 
   \ \_______\ \_______\ \_______\ \__\ \__\ \__\\ _\\ \_______\ \_______\
    \|_______|\|_______|\|_______|\|__|\|__|\|__|\|__|\|_______|\|_______|

"""


def print_boards():   
    """Function to print the boards."""

    print("\n\t\t  USER BOARD\n")

    for x in UserBoard.player_board:
        print(f"{x}")

    print("\n")
    print("\t\t  PC BOARD\n")
    
    # Ocultar o no los barcos del PC
    if SHOW_PC_SHIPS:
        for x in PCBoard.player_board:
            print(f"{x}")

    else:
        for x in INITIAL_BOARD:
            print(f"{x}")


def place_user_ships(ship):
    """Function to place the user ships on his board."""

    correct_coor = False
    correct_orient = False
    
    while not correct_coor:
        coordinates = input("Coordenadas: ")

        coordinate_letter = ''.join(filter(str.isalpha, coordinates))

        try:
            coordinate_num = int(''.join(filter(str.isdigit, coordinates)))

        except ValueError:
            coordinate_num = None

        if coordinate_letter not in LETTER_COOR or str(coordinate_num) not in NUM_COOR:
            print("\nIncorrect coordinates, please, try again.")

            continue

        letters_pos = np.where(UserBoard.player_board == coordinate_letter)[1][0].item()

        coordinate_list = [coordinate_num, letters_pos]

        correct_coor = True

    if not ship == "one_ship":
        while not correct_orient:
            orientation = input("Orientación: ").upper()

            if orientation not in ORIENTATION_LIST:
                print("\nIncorrect orientation, please, try again.")

                continue

            correct_orient = True
    
    else:
        orientation = ""

    UserBoard.place_ships(ship, coordinate_list, orientation)
                    
    clear()

    print(TITLE)
    print("\n\t\t  USER BOARD\n")
    print(f"{UserBoard.player_board}\n")


def user_fire(game_on):
    """Function to process the coordinates of the user atacks."""
    global pc_ships_destroyed, INITIAL_BOARD

    hit = True
    first_shoot = True
    
    while hit:
        if not first_shoot:
            if destrucction:
                pc_ships_destroyed += 1

                if pc_ships_destroyed == 4:
                    game_on = False

                    print("\nHas vencido a tu oponente\n")
                    print(ENHORABUENA)
                    playsound("C:/Users/defco/OneDrive/Escritorio/Cursos/Programación/Cursados/Data Science Bootcamp/2503_dsft_thebridge_anderpena/1-RampUp/Python/Hundir la flota/sounds/win.mp3")

                    break

                print("\nHundido. Sigue así camarada!")

            else:    
                print("\nTocado. Buen disparo!")

        correct_coor = False

        while not correct_coor:
            atack_coordinates = input("\nIndica las coordenadas de disparo: ")

            if atack_coordinates == "Salir":
                game_on = False
                hit = False
            
                clear()

                print("\nGAME OVER.\nTe has rendido al poder superior de tu oponente.\n")
                print(COBARDE)

                break

            atack_coordinate_letter = ''.join(filter(str.isalpha, atack_coordinates))

            try:
                atack_coordinate_num = int(''.join(filter(str.isdigit, atack_coordinates)))

            except ValueError:
                atack_coordinate_num = None

            if atack_coordinate_letter not in LETTER_COOR or str(atack_coordinate_num) not in NUM_COOR:
                print("\nCoordenadas incorrectas, por favor, vuelve a introducirlas.")

                continue

            atack_letters_pos = np.where(UserBoard.player_board == atack_coordinate_letter)[1][0].item()

            atack_coordinate_list = [atack_coordinate_num, atack_letters_pos]

            correct_coor = True
        
        if atack_coordinates != "Salir":
            # Reproduce_video
            player.play()
            time.sleep(3)

            hit, destrucction = UserBoard.fire(PCBoard.player_board if SHOW_PC_SHIPS else INITIAL_BOARD, atack_coordinate_list)

            first_shoot = False
            
            clear()

            print(TITLE)

            print_boards()

    return game_on


def pc_fire(game_on):
    """Function to process the coordinates of the PC atacks."""

    global user_ships_destroyed

    hit = True
    first_shoot = True
    
    while hit:
        if not first_shoot:
            if destrucction:
                user_ships_destroyed += 1

                if user_ships_destroyed == 4:
                    game_on = False

                    print("\nGAME OVER\nTu oponente ha vencido\n")

                    break

                print("\nHundido")

            else:    
                print("\nTocado")

        hit, destrucction  = PCBoard.fire(UserBoard.player_board)

        first_shoot = False

        clear()
        
        print(TITLE)

        print_boards()

    return game_on


clear = lambda: os.system('cls')

clear()

print(TITLE)

open("ship_coordinates.txt", mode="w")

UserBoard = Board("user")
PCBoard = Board("PC")

game_on = True
beggining = True

pc_ships_destroyed = 0
user_ships_destroyed = 0

Instance = vlc.Instance("--fullscreen")
media = Instance.media_new(r"C:/Users/defco/OneDrive/Escritorio/Cursos/Programación/Cursados/Data Science Bootcamp/2503_dsft_thebridge_anderpena/1-RampUp/Python/Hundir la flota/videos/canon.mp4")
player = Instance.media_player_new()
player.set_media(media)
media.get_mrl()

splash = ["splash1", "splash2"]


while game_on:
    if beggining:
        print_boards()
        
        print("\nColoca tus barcos. Para ello indica las coordenadas del bloque inferior del barco como LETRA + NUMERO y la orientación en la que se ha de colocar (N, W, S, E)."
            "Recuerda dejar siempre agua entre los barcos.\n")
        
        # Colocar los barcos del usuario:
        for x in SHIP_LIST:
            match x:
                case "four_ship":
                    print("1 PORTAAVIONES DE LONGITUD 4\n")

                    place_user_ships(SHIP_LIST[0])

                # case "three_ship":
                #     for x in range(2):
                #         print("2 ACORAZADOS DE LONGITUD 3\n")
                        
                #         place_user_ships(SHIP_LIST[1])

                # case "two_ship":
                #     for x in range(3):
                #         print("3 DESTRUCTORES DE LONGITUD 2\n")
                        
                #         place_user_ships(SHIP_LIST[2])

                # case "one_ship":
                #     for x in range(4):
                #         print("4 FRAGATAS DE LONGITUD 1\n")

                #         place_user_ships(SHIP_LIST[3])

        print("Tu contrincante está colocando sus barcos...")

        for x in SHIP_LIST:
            match x:
                case "four_ship":
                    PCBoard.place_ships(x)

                case "three_ship":
                    for y in range(2):
                        PCBoard.place_ships(x)

                case "two_ship":
                    for y in range(3):
                        PCBoard.place_ships(x)

                case "one_ship":
                    for y in range(4):
                        PCBoard.place_ships(x)

        time.sleep(2)

        beggining = False

        clear()

        print("\nCOMIENZA LA PARTIDA")

    else:
        print(TITLE)

        print_boards()

        print("\nEscribe \"Salir\" para rendirte.")

        game_on = user_fire(game_on)

        if not game_on:
            break

        print("\nAgua. Es el turno de tu oponente.")

        # Reproduce splash sound
        playsound(f"./sounds/{random.choice(splash)}.mp3")
        
        print("\nOponente abriendo fuego...")

        time.sleep(2)

        game_on = pc_fire(game_on)

        if not game_on:
            break
        
        print("\nAgua. Es tu turno.")
