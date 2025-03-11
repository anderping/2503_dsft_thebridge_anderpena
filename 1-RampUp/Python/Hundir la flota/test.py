# try:
#     print(int(''.join(filter(str.isdigit, "A"))))

# except ValueError:
#     print(None)


# import numpy as np
# from board import Board, LETTER_COOR, NUM_COOR


# coordinate_letter = ''.join(filter(str.isalpha, "A10"))
# coordinate_num = int(''.join(filter(str.isdigit, "A9")))

# if coordinate_letter in LETTER_COOR:
#     print("YES")

# if str(coordinate_num) in NUM_COOR:
#     print("QUESI")


# list1 = [1, 2]
# list2 = [1, 2]

# print([list1[0], list1[1]] == list2)


coordinate_list = [1, 2]

coordinate_list = [coordinate_list[0] + 1, coordinate_list[1]]

print(coordinate_list)
