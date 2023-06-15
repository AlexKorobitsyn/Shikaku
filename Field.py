import numpy as np


class Field:
    def __init__(self, value, ind, matrix, piece):
        self.ind = ind
        self.piece = piece
        self.value = value
        self.matrix = np.full((len(matrix), len(matrix)), 0)
        np.copyto(self.matrix, matrix)
        self.set()

    def set(self):
        for i in range(len(self.piece)):
            self.matrix[self.piece[i]] = self.value

    def is_solution(self):
        return np.all(self.matrix != 0)

    def __str__(self):
        res = 'Result matrix: \n {}'
        return res.format(self.matrix)