"""Simple statistic functions.

This module has very basic statistic functions for data exploration.
    1. Centrality functions.
    2. Dispersion functions
    3. Correlation functions.


Functions:
  x, y: An iterable
  p : An integer
    - mean(x): Return mean of x.
    - median(x): Return median of x.
    - quantile(x, p): Return p * 100% largest numbers in x.
    - mode(x): Return mode of x.
    - data_range(x): Return range of x.
    - de_mean(x): Return a new iterable with original element subtracted by its mean.
    - variance(x): Return variance of x.
    - standard_deviation(x): Return standard_deviation of x.
    - interquartile_range(x): Return 75% largest number of x minus 25% largest number of x.
    - covariance(x, y): Return covariance of x and y.
    - correlation(x, y): Return correlation of x and y.
"""

from collections import Counter
import math

from data_science_from_scratch.linear_algebra_4.vector import dot_product, sum_of_squares


## 1. Centrality functions
def mean(x):
    """Return mean of an iterable."""
    return sum(x) / len(x)


def median(v):
    """Return median of an iterable."""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        return (sorted_v[midpoint - 1] + sorted_v[midpoint]) / 2


def quantile(x, p):
    """Return quantil of an iterable with given p."""
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    """Return mode of an iterable."""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


## 2. Dispersion functions
def data_range(x):
    """Return range of an iterable."""
    return max(x) - min(x)


def de_mean(x):
    """Return sum of each element that are subtracted by mean of an iterable."""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    """Return variance of an iterable."""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    """Return standard deviation of an iterable."""
    return math.sqrt(variance(x))


def interquartile_range(x):
    """Return interquartile range of an iterable."""
    return quantile(x, 0.75) - quantile(x, 0.25)


## Correlation parts.
def covariance(x, y):
    """Return covariance of two iterables."""
    n = len(x)
    return dot_product(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    """Return correlation of two iterables."""
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0
