import sys
from colorama import Fore, Style

def get_taxicab_distance(puzzle, solved, size):
    pi = puzzle.index(0)
    p1, p2 = pi // size, pi % size
    qi = solved.index(0)
    q1, q2 = qi // size, qi % size
    return abs(p1 - q1) + abs(p2 - q2)

def count_inversions(puzzle, solved, size):
    res = 0
    for i in range(size * size - 1):
        for j in range(i + 1, size * size):
            vi = puzzle[i]
            vj = puzzle[j]
            if solved.index(vi) > solved.index(vj):
                res += 1
    return res


def is_solvable(puzzle, solved, size):
    taxicab_distance = get_taxicab_distance(puzzle, solved, size)
    num_inversions = count_inversions(puzzle, solved, size)
    return taxicab_distance % 2 == num_inversions % 2

def solvable(matrix_snale, matrix, size):
    matrix_snale_aplanado = [number for sublist in matrix_snale for number in sublist]
    if not is_solvable(matrix, matrix_snale_aplanado, size):
        print('Solvable:' + Fore.RED + ' False' + Style.RESET_ALL)
        sys.exit(1)
    else:
        print('Solvable:' + Fore.GREEN + ' True' + Style.RESET_ALL)