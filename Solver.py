import queue

from Field import Field


class Solver:
    def __init__(self, matrix):
        self.points = []
        self.queue = queue.Queue()
        self.grid = matrix
        n = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i, j] != 0:
                    self.points.append([i, j, matrix[i, j], n])
                    n += 1

    def get_point(self, i):
        return self.points[i]

    def get_by_width(self):
        initial = Field(-1, -1, self.grid, [])
        self.queue.put(initial)
        goal = None

        while not self.queue.empty() and goal is None:
            current = self.queue.get()
            if current.is_solution():
                goal = current
            if current.ind + 1 < len(self.points):
                p = self.get_point(current.ind + 1)
                neigh = self.get_neighbours(p[0], p[1], p[2], current.matrix, current.ind + 1)
                for n in range(len(neigh)):
                    self.queue.put(neigh[n])

        return goal

    def check(self, x, y, ind, new_value, mat, dim, value):
        h = []
        w = []
        hb = y - value + 1
        wb = x - dim + 1

        if hb < 0:
            hb = 0
        if wb < 0:
            wb = 0
        while hb <= y and wb <= x:
            arr = []
            for i in range(dim):
                for j in range(value):
                    if (x, y) == (wb + i, hb + j) and hb + j < len(mat) and wb + i < len(mat):
                        arr.append((wb + i, hb + j))
                    if hb + j < len(mat) and wb + i < len(mat) and mat[wb + i, hb + j] == 0:
                        arr.append((wb + i, hb + j))
            if len(arr) == new_value:
                p = Field(new_value, ind, mat, arr)
                h.append(p)
            hb += 1
            if hb > y and wb <= x:
                hb = y - value + 1
                if hb < 0:
                    hb = 0
                wb += 1
        return w, h

    def get_neighbours(self, x, y, value, matrix, ind):
        wt = []
        st = []
        for dim in range(1, value + 1):
            if value % dim == 0:
                w, s = self.check(x, y, ind, value, matrix, dim, int(value / dim))
                st = st + s
                wt = wt + w
        neighbours = wt + st
        return neighbours

