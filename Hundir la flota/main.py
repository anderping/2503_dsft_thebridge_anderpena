from board import Board
import time


UserBoard = Board("user")
PCBoard = Board("PC")

game_on = True
inicio = True

ship_list = ["four_ship", "three_ship", "two_ship", "one_ship"]

while game_on:
    if inicio:
        print("USER BOARD\n")
        print(f"{UserBoard.player_board}\n")

        print("PC BOARD\n")
        print(PCBoard.player_board)
        
        print("\nColoca tus barcos. Para ello indica las coordenadas del bloque inferior del barco como LETRA + NUMERO y la orientación en la que se ha de colocar (N, W, S, E)."
            "Recuerda dejar siempre agua entre los barcos.\n")

        player = "user"

        for x in ship_list:
            match x:
                case "four_ship":
                    print("PORTAAVIONES DE LONGITUD 4\n")
                    print("Coordenadas: ")
                    coordinates = input()
                    print("Orientación: ")
                    orientation = input()
                    print("\n")

                    UserBoard.place_ships(ship_list[0], coordinates, orientation)
                    print("USER BOARD\n")
                    print(f"{UserBoard.player_board}\n")


                case "three_ship":
                    print("ACORAZADO DE LONGITUD 3\n")
                    print("Coordenadas: ")
                    coordinates = input()
                    print("Orientación: ")
                    orientation = input()
                    print("\n")

                    UserBoard.place_ships(ship_list[1], coordinates, orientation)
                    print("USER BOARD\n")
                    print(f"{UserBoard.player_board}\n")

                case "two_ship":
                    print("DESTRUCTOR DE LONGITUD 2\n")
                    print("Coordenadas: ")
                    coordinates = input()
                    print("Orientación: ")
                    orientation = input()
                    print("\n")

                    UserBoard.place_ships(ship_list[2], coordinates, orientation)
                    print("USER BOARD\n")
                    print(f"{UserBoard.player_board}\n")

                case "one_ship":
                    print("FRAGATA DE LONGITUD 1\n")
                    print("Coordenadas: ")
                    coordinates = input()
                    print("Orientación: ")
                    orientation = input()
                    print("\n")

                    UserBoard.place_ships(ship_list[3], coordinates, orientation)
                    print("USER BOARD\n")
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

        print("\nComienza la partida.")

    else:        
        print("USER BOARD\n")
        print(f"{UserBoard.player_board}\n")

        print("PC BOARD\n")
        print(PCBoard.player_board)
        
        hit = True
        first_shoot = True

        while hit:
            if not first_shoot:
                print("Tocado. Buen disparo!\n")

            print("Indica las coordenadas de disparo: ")
            coordinates = input()

            hit = UserBoard.fire(coordinates)

            first_shoot = False
            
            print("USER BOARD\n")    
            print(f"{UserBoard.player_board}\n")

            print("PC BOARD\n")
            print(PCBoard.player_board)

        print("Agua. Es el turno de tu oponente.")

        first_shoot = True

        while hit:
            if not first_shoot:
                print("Tocado\n")

            hit = PCBoard.fire()

            first_shoot = False

            print("USER BOARD\n")    
            print(f"{UserBoard.player_board}\n")

            print("PC BOARD\n")
            print(PCBoard.player_board)

        print("Agua. Es tu turno.")

