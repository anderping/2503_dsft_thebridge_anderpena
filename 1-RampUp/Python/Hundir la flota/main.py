from board import Board
import time
import os
from playsound import playsound
import cv2
from ffpyplayer.player import MediaPlayer


def reproduce_video(video_path, sound_path):
    cap = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)

    while(cap.isOpened()):
        ret,frame = cap.read()
        audio_frame, val = player.get_frame()

        frame = cv2.resize(frame, (1200,700))

        cv2.imshow("video", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        if val != 'eof' and audio_frame is not None:
        #audio
            img, t = audio_frame

    cap.release()
    cv2.destroyAllWindows()



clear = lambda: os.system('cls')

title = r"""
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

enhorabuena = r"""
   __    __        ___  __    _      ___         __    __  _   
  /__\/\ \ \/\  /\/___\/__\  /_\    / __\/\ /\  /__\/\ \ \/_\  
 /_\ /  \/ / /_/ //  // \// //_\\  /__\// / \ \/_\ /  \/ //_\\ 
//__/ /\  / __  / \_// _  \/  _  \/ \/  \ \_/ //__/ /\  /  _  \
\__/\_\ \/\/ /_/\___/\/ \_/\_/ \_/\_____/\___/\__/\_\ \/\_/ \_/
                                                               
"""

print(title)

open("ship_coordinates.txt", mode="w")

UserBoard = Board("user")
PCBoard = Board("PC")

game_on = True
inicio = True

ship_list = ["four_ship", "three_ship", "two_ship", "one_ship"]

pc_ships_destroyed = 0
user_ships_destroyed = 0

while game_on:
    if inicio:
        print("\n\t\t  USER BOARD\n")
        print(f"{UserBoard.player_board}\n")

        print("\t\t  PC BOARD\n")
        print(PCBoard.player_board)
        
        print("\nColoca tus barcos. Para ello indica las coordenadas del bloque inferior del barco como LETRA + NUMERO y la orientación en la que se ha de colocar (N, W, S, E)."
            "Recuerda dejar siempre agua entre los barcos.\n")

        player = "user"

        for x in ship_list:
            match x:
                case "four_ship":
                    print("PORTAAVIONES DE LONGITUD 4\n")
                    coordinates = input("Coordenadas: ")
                    orientation = input("Orientación: ")

                    UserBoard.place_ships(ship_list[0], coordinates, orientation)
                    
                    clear()

                    print(title)
                    print("\n\t\t  USER BOARD\n")
                    print(f"{UserBoard.player_board}\n")


                case "three_ship":
                    print("ACORAZADO DE LONGITUD 3\n")
                    coordinates = input("Coordenadas: ")
                    orientation = input("Orientación: ")

                    UserBoard.place_ships(ship_list[1], coordinates, orientation)
                    
                    clear()
                    
                    print(title)
                    print("\n\t\t  USER BOARD\n")
                    print(f"{UserBoard.player_board}\n")

                case "two_ship":
                    print("DESTRUCTOR DE LONGITUD 2\n")
                    coordinates = input("Coordenadas: ")
                    orientation = input("Orientación: ")

                    UserBoard.place_ships(ship_list[2], coordinates, orientation)
                    
                    clear()

                    print(title)
                    print("\n\t\t  USER BOARD\n")
                    print(f"{UserBoard.player_board}\n")

                case "one_ship":
                    print("FRAGATA DE LONGITUD 1\n")
                    coordinates = input("Coordenadas: ")
                    orientation = input("Orientación: ")

                    UserBoard.place_ships(ship_list[3], coordinates, orientation)
                    
                    clear()

                    print(title)
                    print("\n\t\t  USER BOARD\n")
                    print(f"{UserBoard.player_board}\n")

        print("Tu contrincante está colocando sus barcos...")

        player = "PC"

        for x in ship_list:
            match x:
                case "four_ship":
                    PCBoard.place_ships(ship_list[0])
                case "three_ship":
                    PCBoard.place_ships(ship_list[1])
                case "two_ship":
                    PCBoard.place_ships(ship_list[2])
                case "one_ship":
                    PCBoard.place_ships(ship_list[3])

        time.sleep(2)

        inicio = False

        clear()

        print("\nCOMIENZA LA PARTIDA")

    else:
        print(title)

        print("\n\t\t  USER BOARD\n")
        print(f"{UserBoard.player_board}\n")

        print("\t\t  PC BOARD\n")
        print(PCBoard.player_board)
        
        hit = True
        first_shoot = True


        while hit:
            if not first_shoot:
                if destrucction:
                    pc_ships_destroyed += 1

                    if pc_ships_destroyed == 4:
                        game_on = False

                        print("\nHas vencido a tu oponente\n")
                        print(enhorabuena)
                        playsound("C:/Users/defco/OneDrive/Escritorio/Cursos/Programación/Cursados/Data Science Bootcamp/2503_dsft_thebridge_anderpena/1-RampUp/Python/Hundir la flota/sounds/win.mp3")

                        break

                    print("\nHundido. Sigue así camarada!")

                else:    
                    print("\nTocado. Buen disparo!")

            atack_coordinates = input("\nIndica las coordenadas de disparo: ")
            
            reproduce_video("canon.mp4", "canon.mp3")
            # playsound("C:/Users/defco/OneDrive/Escritorio/Cursos/Programación/Cursados/Data Science Bootcamp/2503_dsft_thebridge_anderpena/1-RampUp/Python/Hundir la flota/sounds/canon.mp3")

            hit, destrucction = UserBoard.fire(PCBoard.player_board, atack_coordinates)

            first_shoot = False
            
            clear()

            print(title)

            print("\n\t\t  USER BOARD\n")    
            print(f"{UserBoard.player_board}\n")

            print("\t\t  PC BOARD\n")
            print(PCBoard.player_board)

        if not game_on:
            break

        print("\nAgua. Es el turno de tu oponente.")

        print("\nOponente abriendo fuego...")
        time.sleep(2)

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
            
            print(title)

            print("\n\t\t  USER BOARD\n")    
            print(f"{UserBoard.player_board}\n")

            print("\t\t  PC BOARD\n")
            print(PCBoard.player_board)

        if not game_on:
            break
        
        print("\nAgua. Es tu turno.")
