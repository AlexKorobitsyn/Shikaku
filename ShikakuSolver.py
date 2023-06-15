import re

import numpy as np

from Solver import Solver


class ShikakuSolver:
    def create_square_matrix(self, height, width, mt):
        if height > width:
            for i in mt:
                i.append(1)
            return mt, 'h'
        else:
            to_add = [1] * len(mt[0])
            mt.append(to_add)
            return mt, 'w'

    def back_to_original(self, mt, key):
        if key == 'h':
            for i in mt:
                i.pop()
            return mt
        else:
            mt.pop()
            return mt

    def parse_input(self, data):
        matrix = []
        parsing_data = data.split('|')
        for a in parsing_data:
            int_arr = []
            line = a.split()
            for x in line:
                int_arr.append(int(x))
            matrix.append(int_arr)
        return matrix

    def get_contains(self, filename):
        matrix = []
        with open(filename, 'r') as f:
            for x in f.readlines():
                int_arr = []
                line = x.split()
                for y in line:
                    int_arr.append(int(y))
                matrix.append(int_arr)
        matrix = np.array(matrix)
        result_matrix = self.return_result_matrix(matrix)
        return result_matrix

    def result_str_to_matrix(self, str_res):
        lines = str_res.split('\n')
        result = []
        lines = lines[1:]
        for line in lines:
            result.append(re.findall(r'\w', line))
        return result

    def solve(self, matrix, document, save):
        result = None
        if matrix is None and document is None:
            mt = input('Enter the game field: ')
            mt = mt[1:-1]
            mt = self.parse_input(mt)
            height = len(mt)
            width = len(mt[0])
            if height != width:
                new_matrix, key = self.create_square_matrix(height, width, mt)
                new_matrix = np.array(new_matrix)
                result = self.return_result_matrix(new_matrix)
                result = self.result_str_to_matrix(result)
                result = self.back_to_original(result, key)
            else:
                result = self.return_result_matrix(np.array(mt))
        elif matrix is not None and document is None:
            mt = self.parse_input(matrix)
            height = len(mt)
            width = len(mt[0])
            if height != width:
                new_matrix, key = self.create_square_matrix(height, width, mt)
                new_matrix = np.array(new_matrix)
                result = self.return_result_matrix(new_matrix)
                result = self.result_str_to_matrix(result)
                result = self.back_to_original(result, key)
            else:
                result = self.return_result_matrix(np.array(mt))
        elif document is not None and matrix is None:
            result = self.get_contains(document)

        if save is None:
            print(result)
        else:
            with open(save, 'w') as f:
                f.write(result)

    def return_result_matrix(self, matrix):
        solver = Solver(matrix)
        goal = solver.get_by_width()
        if goal is not None:
            return str(goal)
        else:
            return "No solution found."
