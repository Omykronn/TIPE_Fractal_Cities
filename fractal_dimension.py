import numpy as np


def count_in_a_box(array: np.ndarray, x: int, y: int, c: int):
    """
    Count the number of ones around the cell (x, y) of array (in a square of length 2c+1)
    :param np.ndarray array: Array to treat
    :param int x: x-coordinate
    :param int y: y_coordinate
    :param int c: Half length less 1
    :return int count: Number of ones founded
    """
    count = 0  # Initialisation
    height, width = array.shape

    for i in range(-c, c + 1):
        for j in range(-c, c + 1):
            if 0 <= x + i < height and 0 <= y + j < width:  # Check if the coordinates are sill in the array
                if array[x + i][y + j] == 1:  # If it is a one, then +1
                    count += 1

    return count


def box_counting_method(array: np.ndarray, r_list: list):
    """
    Determination of the fractal dimension of the pattern represented by array thanks to the box counting method
    :param np.ndarray array: Representation of the pattern
    :param list r_list: List of the length of squares used (each must be odd)
    :return list: List of N(r)
    """
    height, width = array.shape[:2]
    nb_r = len(r_list)
    est_probabilities = []

    for r in r_list:
        est_probabilities.append([0 for _ in range(r**2 + 1)])  # Initialisation of the memory

    for i in range(height):
        for j in range(width):
            for k in range(nb_r):
                m = count_in_a_box(array, i, j, (r_list[k] - 1) // 2)  # Count of 1-cell in the square of size r
                est_probabilities[k][m] += 1

        print(i)  # Indication about the progression

    N_r = [0 for _ in range(nb_r)]  # Initialisation of N(r)

    for k in range(nb_r):
        for m in range(1, r_list[k]**2 + 1):
            N_r[k] += est_probabilities[k][m] / m  # Calculation of N_(r) with est_probabilities

    return N_r
