"""
Name: Steven Sanchez-Jimenez
CS 211, Mini Project: Where's Waldo
February 02, 2023,
Resources: In-class tools
"""

Waldo = 'W'
Other = '.'


def all_row_exists_waldo(matrix: list) -> bool:
    c = 0
    for r in matrix:
        waldo_c = 0
        if Waldo in r:
            waldo_c += 1
        if waldo_c > 0:
            c += 1
    if c >= len(matrix):
        return True
    return False


def all_col_exists_waldo(matrix: list) -> bool:
    if len(matrix) == 0:
        return True
    else:
        for c in range(len(matrix[0])):
            waldo_c = 0
            for r in range(len(matrix)):
                if Waldo in matrix[r][c]:
                    waldo_c +=1
            if waldo_c == 0:
                return False
    return True


def all_row_all_waldo(matrix: list) -> bool:
    for r in matrix:
        for c in r:
            if c != Waldo:
                return False
    return True


def all_col_all_waldo(matrix: list) -> bool:
    for c in matrix:
        for r in c:
            if r != Waldo:
                return False
    return True


def exists_row_all_waldo(matrix: list) -> bool:
    c = 0
    for r in matrix:
        other = 0
        if Other in r:
            other += 1
        if other > 0:
            c += 1
    if c >= len(matrix):
        return False
    return True


def exists_col_all_waldo(matrix: list) -> bool:
    if len(matrix) == 0:
        return False
    else:
        for col in range(len(matrix[0])):
            other = 0
            for row in range(len(matrix)):
                if Other in matrix[row][col]:
                    other += 1
            if other == 0:
                return True
    return False


def exists_row_exists_waldo(matrix: list) -> bool:
    pass


def exists_col_exists_waldo(matrix: list) -> bool:
    pass




