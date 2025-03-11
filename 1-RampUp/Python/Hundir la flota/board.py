import numpy as np
import random
import ast
import copy


FOUR_SHIP_LEN = 4
THREE_SHIP_LEN = 3
TWO_SHIP_LEN = 2
ONE_SHIP_LEN = 1

LETTER_COOR = np.array([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']])
NUM_COOR = np.array([[str(x) for x in range(1, 11)]]).transpose()
BATTLEFIELD = np.array([["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"], 
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"]])
INITIAL_BOARD = np.concatenate((np.concatenate((np.array([[" "]]), NUM_COOR), axis=0), np.concatenate((LETTER_COOR, BATTLEFIELD), axis=0)), axis=1)
INITIAL_BOARD_USER = copy.deepcopy(INITIAL_BOARD)
INITIAL_BOARD_PC = copy.deepcopy(INITIAL_BOARD)


def get_pc_ship_coor(ship_type, direction, player_board, coordinate_list):
    """Function to get the coordinates of each ship for the PC board."""
    
    prohibited_coor_base = [
        (coordinate_list[0], coordinate_list[1] - 1),
        (coordinate_list[0] - 1, coordinate_list[1] - 1),
        (coordinate_list[0] - 1, coordinate_list[1]),
        (coordinate_list[0] - 1, coordinate_list[1] + 1),
        (coordinate_list[0], coordinate_list[1] + 1),
        (coordinate_list[0] + 1, coordinate_list[1] + 1),
        (coordinate_list[0] + 1, coordinate_list[1]),
        (coordinate_list[0] + 1, coordinate_list[1] - 1)
        ]
       
    # FOUR_SHIP
    if ship_type == "four_ship" and direction == "Vertical":
        coordinate_list = [random.randint(4, 7), random.randint(1, 10)]

    elif ship_type == "four_ship" and direction == "Horizontal":
        coordinate_list = [random.randint(1, 10), random.randint(4, 7)]

    # THREE_SHIP        
    elif ship_type == "three_ship" and direction == "Vertical":
        coordinate_list = [random.randint(3, 8), random.randint(1, 10)]
        delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

        segment = 0
        all_checked = False

        while not all_checked:
            while player_board[coordinate_list[0], coordinate_list[1]] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == coordinate_list:
                coordinate_list = [random.randint(3, 8), random.randint(1, 10)]
                delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

            segment += 1

            if player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == [coordinate_list[0] + segment, coordinate_list[1]]:
                coordinate_list = [random.randint(3, 8), random.randint(1, 10)]
                delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

                segment = 0

                continue
                
            segment += 1

            if player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == [coordinate_list[0] + segment, coordinate_list[1]]:
                coordinate_list = [random.randint(3, 8), random.randint(1, 10)]

                segment = 0
            
            else:
                all_checked = True


    elif ship_type == "three_ship" and direction == "Horizontal":
        coordinate_list = [random.randint(1, 10), random.randint(3, 8)]
        delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

        segment = 0
        all_checked = False

        while not all_checked:
            while player_board[coordinate_list[0], coordinate_list[1]] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == coordinate_list:
                coordinate_list = [random.randint(1, 10), random.randint(3, 8)]
                delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)
            
            segment += 1

            if player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == [coordinate_list[0], coordinate_list[1] + segment]:
                coordinate_list = [random.randint(1, 10), random.randint(3, 8)]
                delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

                segment = 0
            
                continue

            segment += 1

            if player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == [coordinate_list[0], coordinate_list[1] + segment]:
                coordinate_list = [random.randint(1, 10), random.randint(3, 8)]

                segment = 0

            else:
                all_checked = True

    # TWO_SHIP
    elif ship_type == "two_ship" and direction == "Vertical":
        coordinate_list = [random.randint(2, 9), random.randint(1, 10)]
        delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

        segment = 0
        all_checked = False

        while not all_checked:
            while player_board[coordinate_list[0], coordinate_list[1]] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == coordinate_list:
                coordinate_list = [random.randint(2, 9), random.randint(1, 10)]
                delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)
            
            segment += 1

            if player_board[coordinate_list[0] + segment, coordinate_list[1]] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == [coordinate_list[0] + segment, coordinate_list[1]]:
                coordinate_list = [random.randint(2, 9), random.randint(1, 10)]
                delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

                segment = 0
            
            else:
                all_checked = True

    elif ship_type == "two_ship" and direction == "Horizontal":
        coordinate_list = [random.randint(1, 10), random.randint(2, 9)]
        delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

        segment = 0
        all_checked = False

        while not all_checked:
            while player_board[coordinate_list[0], coordinate_list[1]] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == coordinate_list:
                coordinate_list = [random.randint(1, 10), random.randint(2, 9)]
                delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

            segment += 1

            if player_board[coordinate_list[0], coordinate_list[1] + segment] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == [coordinate_list[0], coordinate_list[1] + segment]:
                coordinate_list = [random.randint(1, 10), random.randint(2, 9)]

                segment = 0
            
            else:
                all_checked = True

    # ONE SHIP
    elif ship_type == "one_ship":
        coordinate_list = [random.randint(1, 10), random.randint(1, 10)]
        delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

        while player_board[coordinate_list[0], coordinate_list[1]] == "▣" or any([x, y] for x, y in delimited_prohibited_coor) == coordinate_list:
            coordinate_list = [random.randint(1, 10), random.randint(1, 10)]
            delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor_base)

    return coordinate_list


def delimit_prohibited_coor(possible_coor, initial_prohibited_coor):
    """Function to delimit de prohibit coordinates where no ships can be placed when these are placed near the border of the boards."""
    
    delimited_prohibited_coor = initial_prohibited_coor.copy()

    if possible_coor[0] == 0:
        del delimited_prohibited_coor[1:4]

    elif possible_coor[0] == 10:
        del delimited_prohibited_coor[5:8]

    elif possible_coor[1] == 0:
        delimited_prohibited_coor = delimited_prohibited_coor[2:7]

    elif possible_coor[1] == 10:
        del delimited_prohibited_coor[3:6]

    return delimited_prohibited_coor


def copy_ships_on_board(orientation, player_board, ship_len, coordinate_list, player, ship_type):
    """Function to copy the ships on the player board."""
    
    if orientation == 'E' or orientation == "":
        for x in range(ship_len):
            player_board[coordinate_list[0], coordinate_list[1] + x] = "▣"

            add_to_dict(coord_dic, player, ship_type, [coordinate_list[0], coordinate_list[1] + x])

    elif orientation == 'N':
        for x in range(ship_len):
            player_board[coordinate_list[0] - x, coordinate_list[1]] = "▣"

            add_to_dict(coord_dic, player, ship_type, [coordinate_list[0] - x, coordinate_list[1]])
                    
    elif orientation == 'W':
        for x in range(ship_len):
            player_board[coordinate_list[0], coordinate_list[1] - x] = "▣"

            add_to_dict(coord_dic, player, ship_type, [coordinate_list[0], coordinate_list[1] - x])

    elif orientation == 'S':
        for x in range(ship_len):
            player_board[coordinate_list[0] + x, coordinate_list[1]] = "▣"

            add_to_dict(coord_dic, player, ship_type, [coordinate_list[0] + x, coordinate_list[1]])


def check_ship_hit(player, coor):
    """Function to check on the "ship_coordinates.txt" document if the atack coordinates correspond to an opponent ship coordinate."""

    with open("ship_coordinates.txt", "r") as f:
        coor_dict = ast.literal_eval(f.read())

    for (ship_name, saved_coordinates) in coor_dict[player].items():
        if coor in saved_coordinates:
            return ship_name


def add_to_dict(data, player, ship, coor):
    """Function to add a new ship to the "ship_coordinates.txt" document."""

    if player not in data:
        data[player] = {}
    if ship not in data[player]:
        data[player][ship] = []

    data[player][ship].append(coor)

    with open("ship_coordinates.txt", "w") as f:
        f.write(str(dict(data)))


def check_ship_destroyed(player_hits, ship_hit):
    """Function to check in the "ship_coordinates.txt" document if a ship has been destroyed completely."""
    
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
    def __init__(self, player, user_board=INITIAL_BOARD_USER, pc_board=INITIAL_BOARD_PC):
        self.player = player

        if player == 'user':
            self.player_board = user_board
            self.opponent = "PC"
        else:
            self.player_board = pc_board
            self.opponent = "user"

    def place_ships(self, ship_type, coordinate_list=[0, 0], orientation=""):
        global coord_dic

        ship_len = 0
       
        match ship_type:
            case "four_ship":
                ship_len = FOUR_SHIP_LEN

            case "three_ship":
                ship_len = THREE_SHIP_LEN

            case "two_ship":
                ship_len = TWO_SHIP_LEN

            case "one_ship":
                ship_len = ONE_SHIP_LEN

        # PARAMETROS POSICION BARCOS PC:
        if self.player == "PC":
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

            coordinate_list = get_pc_ship_coor(ship_type, direction, self.player_board, coordinate_list)

        # COLOCAR BARCOS EN LOS TABLEROS:
        copy_ships_on_board(orientation, self.player_board, ship_len, coordinate_list, self.player, ship_type)


    def fire(self, opponent_board, atack_coordinate_list=[]):
        global coord_dic

        if self.player == "PC":
            atack_coordinate_list = [random.randint(1, 10), random.randint(1, 10)]

        if opponent_board[atack_coordinate_list[0], atack_coordinate_list[1]] == "▣":
            opponent_board[atack_coordinate_list[0], atack_coordinate_list[1]] = "⛝"

            ship_type = check_ship_hit(self.opponent, atack_coordinate_list)
            
            add_to_dict(coord_dic, f"{self.player}_hits", ship_type, [atack_coordinate_list[0], atack_coordinate_list[1]])

            destruction = check_ship_destroyed(f"{self.player}_hits", ship_type)

            hit = True

        else:
            opponent_board[atack_coordinate_list[0], atack_coordinate_list[1]] = "⧆"

            destruction = False

            hit = False

        return hit, destruction
    