import numpy as np


class Ships():
    def __init__(self):
        self.four_ship = np.array(["▣"]*4) # 4 barcos de 1 posición de eslora
        self.three_ship = np.array(["▣"]*3) # * 3 barcos de 2 posiciones de eslora
        self.two_ship = np.array(["▣"]*2) # * 2 barcos de 3 posiciones de eslora
        self.one_ship = np.array(["▣"]) # * 1 barco de 4 posiciones de eslora
