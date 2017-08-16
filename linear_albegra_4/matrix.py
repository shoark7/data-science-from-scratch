"""Matrix functions.

Basic matrix functions.
Of course we use list in a list for matrix too.
So matrix here is a list.

Also we assume we use only two dimensional matrix.


Functions:
    - shape: (matrix1). Return the shape of a matrix.
    - get_row: (matrix1, index). Return the i'th row of the matrix
    - get_column: (matrix1, index). Return the i'th column of the matrix
    - make_matrix: (num_rows, num_cols, number_generator_function)
                   With number of rows, cols and number generator function given,
                   return a new matrix. number_generator_function should be a function or a callable
                   which takes i, j index as arguments. And it must return some values for elements.
    - is_diagonal: (i, j). Return True if i and j are same. This is for identity element of a
    matrix.
"""


def shape(A):
    """Return the shape of a matrix."""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    """Return the row of given matrix and index."""
    return A[i]


def get_column(A, j):
    """Return the column of given matrix and index."""
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, number_generator_function):
    """Return a new matrix with given num_rows, num_cols and number generator function."""
    return [[number_generator_function(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    """Return True if i and j are same."""
    return 1 if i == j else 0
