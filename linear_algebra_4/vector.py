"""Vector implementation for further studies.

This module implements basic vector functions using list.
So vector here is a list.
Using list for vector calculations sucks but fits well for purpose of this project.

Functions:
    - vector_add: (v1, v2). Return a new vector with each element of two vectors summed.
    - vector_subtract: (v1, v2). Return a new vector with each element of two vectors subtracted.
    - scalar_multiply: (int n, vector v). Return a new vector of which every element multiplied by integer n.
    - vector_mean: (list of vectors). Return a new vector of which every element averaged from input
    - dot_product: (v1, v2). Get doc product from two vectors.
    - sum_of_squares: (v). Get squared sum of all elements in a vector.
    - magnitude_of_vector: (v). Get the magnitude of a vector.
    - squared_distance(v1, v2). Get squared distance from v1 to v2.
    - distance(v1, v2). Get magnitude of two vectors.
"""

from functools import partial, reduce
import math


def vector_add(v, w):
    """벡터의 각 성분끼리 더함."""
    if len(v) != len(w):
        raise ValueError("Dimensions of two vectors must be same")
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """벡터의 각 성분끼리 뺌."""
    if len(v) != len(w):
        raise ValueError("Dimensions of two vectors must be same")
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# 두 개 이상의 벡터들의 각 성분끼리 더하는 법

# way 1.
# def vector_sum(vectors):
    # result = vectors[0]
    # for vector in vectors[1:]:
        # result = vector_add(result, vector)
    # return result

# way2
# def vector_sum(vectors):
    # return reduce(vector_add, vectors)


## way3
vector_sum = partial(reduce, vector_add)


def scalar_multiply(n, v):
    """스칼라 곱"""
    return [n * v_i for v_i in v]


def vector_mean(vectors):
    """Get average of each element in a vector list."""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot_product(v, w):
    """Dot product of a vector."""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """Get squared sum of a vector."""
    return dot_product(v, v)


def magnitude_of_vector(v):
    """Get squared sum of all elements in a vector."""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """Squared sum of vector subtraction."""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    """Get the distance(magnitude) between two vectors."""
    return magnitude_of_vector(vector_subtract(v, w))
