import argparse

from ShikakuSolver import ShikakuSolver

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Shikaku')
    parser.add_argument('-mt', '--matrix', type=str, metavar='', help='Matrix with a field for the game')
    parser.add_argument('-doc', '--document', type=str, metavar='', help='Document with a field for the game')
    parser.add_argument('-save', '--save', type=str, metavar='', help='The path of the file in which to save result')
    args = parser.parse_args()
    matrix = args.matrix
    document = args.document
    save = args.save

    solver = ShikakuSolver()
    solver.solve(matrix, document, save)