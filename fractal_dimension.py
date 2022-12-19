import numpy as np

from PIL import Image
from math import log
from map_treatement import extract


def count_in_a_box(array: np.ndarray, x: int, y: int, c: int):
    """
    Count the number of ones around the cell (x, y) of array (in a square of length 2c+1)
    :param np.ndarray array: Array to treat
    :param int x: x-coordinate
    :param int y: y_coordinate
    :param int c: Half length less 1
    :return int count: Number of ones founded for each box
    """
    count = [0 for _ in range(c + 1)]
    height, width = array.shape[:2]

    for i in range(-c, c + 1):
        for j in range(-c, c + 1):
            if 0 <= x + i < height and 0 <= y + j < width:  # Check if the coordinates are sill in the array
                if array[x + i][y + j] == 1:  # If it is a one, then +1 for the square of corresponding length
                    count[max(abs(i), abs(j))] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]  # Final addition to determine the number in each box

    return count


def box_counting_method(array: np.ndarray, r_max: int):
    """
    Determination of the fractal dimension of the pattern represented by array thanks to the box counting method
    :param np.ndarray array: Representation of the pattern
    :param r_max: Maximum length of the box (must be odd)
    :return list: List of N(r)
    """
    height, width = array.shape[:2]
    nb_r = (r_max + 1) // 2
    headcount = []

    for k in range(nb_r):
        headcount.append([0 for _ in range((2*k + 1)**2 + 1)])  # Initialisation of the memory

    for i in range(height):
        for j in range(width):
            # Count of 1-cell in all the squares of length less than r_max
            temp_count = count_in_a_box(array, i, j, nb_r - 1)

            # Final count for this cell
            for k in range(len(temp_count)):
                headcount[k][temp_count[k]] += 1

        if i % 10 == 0:
            print("BOX COUNTING", int(i * 10000 / height) / 100, "%")  # Indication about the progression

    N_r = [0 for _ in range(nb_r)]  # Initialisation of N(r)

    for k in range(nb_r):
        for m in range(1, (2*k+1)**2 + 1):
            N_r[k] += headcount[k][m] / m  # Calculation of N_(r) with est_probabilities

    return N_r


def analyse_one_cell(image_dir: str, r_max: int):
    """
    Procedure of analysis on one cell of the original image (ie on one subdivision)
    :param str image_dir: Directory to the image
    :param int r_max: Maximum length of the box (must be odd)
    :return: None
    """
    picture = extract(np.array(Image.open(image_dir)))
    data = box_counting_method(picture, r_max)  # Box Counting Method

    absi = []
    ordo = []

    try:  # Try and catch structure in case of a blank cell : log(0) is not defined
        for i in range(len(data)):
            absi.append(-log(2*i+1))
            ordo.append(log(data[i]))

        # Determination of the fractal dimension with a linear regression between log(1/r) and log(N(r))
        regression_data = np.polyfit(absi, ordo, 1)

        a = regression_data[0]  # The fractal dimension is the slope
    except ValueError:
        a = 0

    return a
