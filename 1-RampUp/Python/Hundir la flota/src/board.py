import numpy as np
import random
import ast
import copy


SHIP_SIZES = {"four_ship": 4, "three_ship": 3, "two_ship": 2, "one_ship": 1}

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


def get_random_coordinate(ship_type, direction):
    """Generate a random starting coordinate based on ship type and direction."""

    ship_ranges = {
        "four_ship": (4, 7),
        "three_ship": (3, 8),
        "two_ship": (2, 9),
        "one_ship": (1, 10)
    }
    
    if direction == "Vertical":
        return [random.randint(ship_ranges[ship_type][0], ship_ranges[ship_type][1]), random.randint(1, 10)]
    
    else:
        return [random.randint(1, 10), random.randint(ship_ranges[ship_type][0], ship_ranges[ship_type][1])]


def delimit_prohibited_coor(possible_coor, initial_prohibited_coor):
    """Adjust prohibited coordinates based on board boundaries."""
    
    delimited_prohibited_coor = initial_prohibited_coor.copy()

    if possible_coor[0] == 1:
        del delimited_prohibited_coor[1:4]

    elif possible_coor[0] == 10:
        del delimited_prohibited_coor[5:8]

    elif possible_coor[1] == 1:
        delimited_prohibited_coor = delimited_prohibited_coor[2:7]

    elif possible_coor[1] == 10:
        del delimited_prohibited_coor[3:6]

    return delimited_prohibited_coor


def is_valid_position(coordinate_list, player_board, prohibited_coor, ship_type, direction, segment=0):
    """Recursively check if the ship can be placed in the given position."""

    if segment == SHIP_SIZES[ship_type]:
        return True
    
    x, y = coordinate_list
    new_pos = [x + segment, y] if direction == "Vertical" else [x, y + segment]
    
    # Dejo sin implementar la funcionalidad para que los barcos se coloquen con agua alrededor siempre
    if player_board[new_pos[0], new_pos[1]] == "▣": # or tuple(new_pos) in prohibited_coor:
        return False
    
    return is_valid_position(coordinate_list, player_board, prohibited_coor, ship_type, direction, segment + 1)


def get_pc_ship_coor(ship_type, direction, player_board):
    """Find a valid coordinate for the ship placement using recursion."""
    
    while True:
        coordinate_list = get_random_coordinate(ship_type, direction)
        
        prohibited_coor = [
            (coordinate_list[0], coordinate_list[1] - 1),
            (coordinate_list[0] - 1, coordinate_list[1] - 1),
            (coordinate_list[0] - 1, coordinate_list[1]),
            (coordinate_list[0] - 1, coordinate_list[1] + 1),
            (coordinate_list[0], coordinate_list[1] + 1),
            (coordinate_list[0] + 1, coordinate_list[1] + 1),
            (coordinate_list[0] + 1, coordinate_list[1]),
            (coordinate_list[0] + 1, coordinate_list[1] - 1)
        ]
        
        delimited_prohibited_coor = delimit_prohibited_coor(coordinate_list, prohibited_coor)
        
        if is_valid_position(coordinate_list, player_board, delimited_prohibited_coor, ship_type, direction):
            break

    return coordinate_list


def add_to_dict(data, player, ship, coor):
    """Add a new ship to the "ship_coordinates.txt" document."""

    if player not in data:
        data[player] = {}
    if ship not in data[player]:
        data[player][ship] = []

    data[player][ship].append(coor)

    with open("ship_coordinates.txt", "w") as f:
        f.write(str(dict(data)))


def copy_ships_on_board(orientation, player_board, ship_len, coordinate_list, player, ship_type):
    """Copy the ships on the player board."""
    
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
    """Check on the "ship_coordinates.txt" document if the atack coordinates correspond to an opponent ship coordinate."""

    with open("ship_coordinates.txt", "r") as f:
        coor_dict = ast.literal_eval(f.read())

    for (ship_name, saved_coordinates) in coor_dict[player].items():
        if coor in saved_coordinates:
            return ship_name


def check_ship_destroyed(player_hits, ship_hit):
    """Check in the "ship_coordinates.txt" document if a ship has been destroyed completely."""
    
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

    def place_ships(self, ship_type, coordinate_list=[], orientation=""):
        global coord_dic

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

            coordinate_list = get_pc_ship_coor(ship_type, direction, self.player_board)

        # COLOCAR BARCOS EN LOS TABLEROS:
        copy_ships_on_board(orientation, self.player_board, SHIP_SIZES[ship_type], coordinate_list, self.player, ship_type)


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
    