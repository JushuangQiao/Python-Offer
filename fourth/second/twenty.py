# coding=utf-8
"""
按从外到里的顺序顺时针打印矩阵
每一圈的开始位置总是坐上角元素[0, 0], [1, 1]...
"""


def print_matrix(matrix):
    """
    :param matrix: [[]]
    """
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    start = 0
    ret = []
    while start * 2 < rows and start * 2 < cols:
        print_circle(matrix, start, rows, cols, ret)
        start += 1
    print ret


def print_circle(matrix, start, rows, cols, ret):
    row = rows - start - 1  # 最后一行
    col = cols - start - 1
    # left->right
    for c in range(start, col+1):
        ret.append(matrix[start][c])
    # top->bottom
    if start < row:
        for r in range(start+1, row+1):
            ret.append(matrix[r][col])
    # right->left
    if start < row and start < col:
        for c in range(start, col)[::-1]:
            ret.append(matrix[row][c])
    # bottom->top
    if start < row and start < col:
        for r in range(start+1, row)[::-1]:
            ret.append(matrix[r][start])


if __name__ == '__main__':
    """
    mat = [[1, 2, 3],
           [5, 6, 7],
           [9, 10, 11]]
    mat = [[]]
    mat = [[1]]
    mat = [[1, 2, 3, 4]]
    mat = [[1], [2], [3], [4]]
    """
    mat = [[1, 2],
           [5, 6]]
    print_matrix(mat)
