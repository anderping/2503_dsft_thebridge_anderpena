import numpy as np
from ships import Ships
import random
import ast


def save_data(data):
    with open("ship_coordinates.txt", "w") as f:
        f.write(str(dict(data))) 


def check_ship_hit(player, coor):
    with open("ship_coordinates.txt", "r") as f:
        coor_dict = ast.literal_eval(f.read())

    for (ship_name, saved_coordinates) in coor_dict[player].items():
        if coor in saved_coordinates:
            return ship_name


def add_to_dict(data, player, ship, coor):
    if player not in data:
        data[player] = {}
    if ship not in data[player]:
        data[player][ship] = []

    data[player][ship].append(coor)

    save_data(data)


def check_ship_destroyed(player_hits, ship_hit):
    with open("ship_coordinates.txt", "r") as f:
        coor_dict = ast.literal_eval(f.read())

    for (ship_name, saved_coordinates) in coor_dict[player_hits].items():
        if ship_hit == ship_name:
            if ship_name == "four_ship":
                if len(saved_coordinates) == 4:
                    return True
                
            if ship_name == "three_ship":
                if len(saved_coordinates) == 3:
                    return True
                
            if ship_name == "two_ship":
                if len(saved_coordinates) == 2:
                    return True
                
            if ship_name == "one_ship":
                if len(saved_coordinates) == 1:
                    return True
    
    return False
    

coord_dic = {}


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
        global coord_dic

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

            letters_pos = np.where(self.player_board == coordinate_letter)[1][0].item()

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

            elif ship_type == "four_ship" and direction == "Horizontal":
                coordinate_list = [random.randint(1, 10), random.randint(4, 7)]


            elif ship_type == "three_ship" and direction == "Vertical":
                coordinate_list = [random.randint(3, 8), random.randint(1, 10)]

                segment = 0
                all_checked = False

                while not all_checked:
                    while self.player_board[coordinate_list[0], coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(3, 8), random.randint(1, 10)]
                    
                    segment += 1

                    if self.player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(3, 8), random.randint(1, 10)]

                        segment = 0

                        continue
                        
                    segment += 1

                    if self.player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(3, 8), random.randint(1, 10)]

                        segment = 0
                    
                    else:
                        all_checked = True

            elif ship_type == "three_ship" and direction == "Horizontal":
                coordinate_list = [random.randint(1, 10), random.randint(3, 8)]

                segment = 0
                all_checked = False

                while not all_checked:
                    while self.player_board[coordinate_list[0], coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(3, 8)]
                    
                    segment += 1

                    if self.player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(3, 8)]

                        segment = 0
                    
                        continue

                    segment += 1

                    if self.player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(3, 8)]

                        segment = 0

                    else:
                        all_checked = True


            elif ship_type == "two_ship" and direction == "Vertical":
                coordinate_list = [random.randint(2, 9), random.randint(1, 10)]

                segment = 0
                all_checked = False

                while not all_checked:
                    while self.player_board[coordinate_list[0], coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(2, 9), random.randint(1, 10)]
                    
                    segment += 1

                    if self.player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(2, 9), random.randint(1, 10)]

                        segment = 0
                    
                    else:
                        all_checked = True


            elif ship_type == "two_ship" and direction == "Horizontal":
                coordinate_list = [random.randint(1, 10), random.randint(2, 9)]

                segment = 0
                all_checked = False

                while not all_checked:
                    while self.player_board[coordinate_list[0], coordinate_list[1]] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(2, 9)]
                    
                    segment += 1

                    if self.player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣":
                        coordinate_list = [random.randint(1, 10), random.randint(2, 9)]

                        segment = 0
                    
                    else:
                        all_checked = True


            elif ship_type == "one_ship":
                coordinate_list = [random.randint(1, 10), random.randint(1, 10)]

                while self.player_board[coordinate_list[0], coordinate_list[1]] == "▣":
                    coordinate_list = [random.randint(1, 10), random.randint(1, 10)]
    

# COLOCAR BARCOS:
        if orientation == 'E':
            for x in range(ship_len):
                self.player_board[coordinate_list[0], coordinate_list[1] + x] = "▣"

                add_to_dict(coord_dic, self.player, ship_type, [coordinate_list[0], coordinate_list[1] + x])

        elif orientation == 'N':
            for x in range(ship_len):
                self.player_board[coordinate_list[0] - x, coordinate_list[1]] = "▣"

                add_to_dict(coord_dic, self.player, ship_type, [coordinate_list[0] - x, coordinate_list[1]])
                        
        elif orientation == 'W':
            for x in range(ship_len):
                self.player_board[coordinate_list[0], coordinate_list[1] - x] = "▣"

                add_to_dict(coord_dic, self.player, ship_type, [coordinate_list[0], coordinate_list[1] - x])

        elif orientation == 'S':
            for x in range(ship_len):
                self.player_board[coordinate_list[0] + x, coordinate_list[1]] = "▣"

                add_to_dict(coord_dic, self.player, ship_type, [coordinate_list[0] + x, coordinate_list[1]])


    def fire(self, opponent_board, atack_coordinates=""):
        if self.player == "user":
            attack_coordinate_letter = ''.join(filter(str.isalpha, atack_coordinates))
            attack_coordinate_num = int(''.join(filter(str.isdigit, atack_coordinates)))

            attack_letters_pos = np.where(self.player_board == attack_coordinate_letter)[1][0].item()

            attack_coordinate_list = [attack_coordinate_num, attack_letters_pos]
        
            if opponent_board[attack_coordinate_list[0], attack_coordinate_list[1]] == "▣":
                opponent_board[attack_coordinate_list[0], attack_coordinate_list[1]] = "⛝"

                ship_type = check_ship_hit("PC", attack_coordinate_list)
                
                add_to_dict(coord_dic, "user_hits", ship_type, [attack_coordinate_list[0], attack_coordinate_list[1]])

                destruction = check_ship_destroyed("user_hits", ship_type)

                hit = True

            else:
                opponent_board[attack_coordinate_list[0], attack_coordinate_list[1]] = "⧆"

                hit = False

        else:
            attack_coordinate_list = [random.randint(1, 10), random.randint(1, 10)]

            if opponent_board[attack_coordinate_list[0], attack_coordinate_list[1]] == "▣":
                opponent_board[attack_coordinate_list[0], attack_coordinate_list[1]] = "⛝"
                
                ship_type = check_ship_hit("user", attack_coordinate_list)
                
                add_to_dict(coord_dic, "PC_hits", ship_type, [attack_coordinate_list[0], attack_coordinate_list[1]])

                destruction = check_ship_destroyed("PC_hits", ship_type)
                
                hit = True

            else:
                opponent_board[attack_coordinate_list[0], attack_coordinate_list[1]] = "⧆"

                hit = False

        return hit, destruction
    