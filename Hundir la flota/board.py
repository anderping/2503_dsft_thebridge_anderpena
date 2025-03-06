import numpy as np
from ships import Ships
import random
from main import PCBoard


class Board():
    letter_coor = np.array([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']])
    num_coor = np.array([[str(x) for x in range(1, 11)]]).transpose()
    battlefield = np.array([["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"], 
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"]])
    initial_board_user = np.concatenate((np.concatenate((np.array([[" "]]), num_coor), axis=0), np.concatenate((letter_coor, battlefield), axis=0)), axis=1)
    initial_board_PC = initial_board_user.copy()

    def __init__(self, player, user_board=initial_board_user, PC_board=initial_board_PC):
        self.player = player

        if player == 'user':
            self.player_board = user_board
        else:
            self.player_board = PC_board

    def place_ships(self, ship_type, coordinates="", orientation=""):
        Ship = Ships()
        
        match ship_type:
            case "four_ship":
                ship_len = len(Ship.four_ship)

            case "three_ship":
                ship_len = len(Ship.three_ship)

            case "two_ship":
                ship_len = len(Ship.two_ship)

            case "one_ship":
                ship_len = len(Ship.one_ship)


        if self.player == "user":
            coordinate_letter = ''.join(filter(str.isalpha, coordinates))
            coordinate_num = int(''.join(filter(str.isdigit, coordinates)))

            letters_pos = np.where(self.player_board == coordinate_letter)[1][0]

            coordinate_list = [coordinate_num, letters_pos]

#PARAMETROS POSICION BARCOS PC:
        else:
            direction = random.choice(["Vertical", "Horizontal"])

            sign = random.choice([1, -1])

            if direction == "Vertical" and sign == 1:
                orientation = "N"
            
            elif direction == "Vertical" and sign == -1:
                orientation = "S"

            elif direction == "Horizontal" and sign == 1:
                orientation = "E"
            
            elif direction == "Horizontal" and sign == -1:
                orientation = "W"


            if ship_type == "four_ship" and direction == "Vertical":
                coordinate_list = [random.randint(4, 7), random.randint(1, 10)]

            if ship_type == "four_ship" and direction == "Horizontal":
                coordinate_list = [random.randint(1, 10), random.randint(4, 7)]


            if ship_type == "three_ship" and direction == "Vertical":
                coordinate_list = [random.randint(3, 10), random.randint(1, 10)]

                segment = 0
                all_checked = False

                while not all_checked:
                    while self.player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(3, 10), random.randint(1, 10)]
                    
                    segment += 1

                    if self.player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(3, 10), random.randint(1, 10)]

                        segment = 0

                        continue
                        
                    segment += 1

                    if self.player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(3, 10), random.randint(1, 10)]

                        segment = 0
                    
                    else:
                        all_checked = True

            if ship_type == "three_ship" and direction == "Horizontal":
                coordinate_list = [random.randint(1, 10), random.randint(3, 10)]

                segment = 0
                all_checked = False

                while not all_checked:
                    while self.player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(3, 10)]
                    
                    segment += 1

                    if self.player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(3, 10)]

                        segment = 0
                    
                        continue

                    segment += 1

                    if self.player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(3, 10)]

                        segment = 0

                    else:
                        all_checked = True


            if ship_type == "two_ship" and direction == "Vertical":
                coordinate_list = [random.randint(2, 10), random.randint(1, 10)]

                segment = 0
                all_checked = False

                while not all_checked:
                    while self.player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(2, 10), random.randint(1, 10)]
                    
                    segment += 1

                    if self.player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(2, 10), random.randint(1, 10)]

                        segment = 0
                    
                    else:
                        all_checked = True


            if ship_type == "two_ship" and direction == "Horizontal":
                coordinate_list = [random.randint(1, 10), random.randint(2, 10)]

                segment = 0
                all_checked = False

                while not all_checked:
                    while self.player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(2, 10)]
                    
                    segment += 1

                    if self.player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(2, 10)]

                        segment = 0
                    
                    else:
                        all_checked = True


            if ship_type == "one_ship":
                coordinate_list = [random.randint(1, 10), random.randint(1, 10)]

                while self.player_board[coordinate_list[0], coordinate_list[1]] == "▣":
                    coordinate_list = [random.randint(1, 10), random.randint(1, 10)]           

# COLOCAR BARCOS:
        if orientation == 'E':
            for x in range(ship_len):
                self.player_board[coordinate_list[0], coordinate_list[1] + x] = "▣"

        elif orientation == 'N':
            for x in range(ship_len):
                self.player_board[coordinate_list[0] - x, coordinate_list[1]] = "▣"
                        
        elif orientation == 'W':
            for x in range(ship_len):
                self.player_board[coordinate_list[0], coordinate_list[1] - x] = "▣"

        elif orientation == 'S':
            for x in range(ship_len):
                self.player_board[coordinate_list[0] + x, coordinate_list[1]] = "▣"


    def fire(self, atack_coordinates=""):
        if self.player == "user":
            self.player_board = PC_board

            attack_coordinate_letter = ''.join(filter(str.isalpha, atack_coordinates))
            attack_coordinate_num = int(''.join(filter(str.isdigit, atack_coordinates)))

            attack_letters_pos = np.where(self.player_board == attack_coordinate_letter)[1][0]

            attack_coordinate_list = [attack_coordinate_num, attack_letters_pos]
        
            if self.PCBoard.[attack_coordinate_list[0], attack_coordinate_list[1]] == "▣":
                

                hit = True


        return hit
