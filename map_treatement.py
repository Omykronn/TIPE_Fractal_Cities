import math
import numpy as np

from PIL import Image
from os import mkdir


# Tools

def distance_euclid(v1: tuple, v2: tuple):
    """
    Distance associated to the euclidian norm in R³
    :param tuple v1: 3-tuple n°1
    :param tuple v2: 3-tuple n°2
    :return float: Distance between vector1 and vector2
    """
    return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2 + (v1[2] - v2[2]) ** 2)


# Methods

def similar_color(pixel: tuple, color_tgt: tuple):
    """
    Comparaison based on the distance between the two colors (in the R³ space) : 27 seems to be the best value
    :param tuple pixel: Pixel to compare
    :param tuple color_tgt: Pixel of reference
    :return bool: Result of the comparaison
    """
    return distance_euclid(color_tgt, pixel) <= 27


def darker_color(pixel: tuple, color_tgt: tuple):
    """
    Comparaison based on the norms of the two colors (in the R³ space)
    :param tuple pixel: Pixel to compare
    :param tuple color_tgt: Pixel of reference
    :return bool: Result of the comparaison
    """
    return distance_euclid(pixel, (0, 0, 0)) <= distance_euclid(color_tgt, (0, 0, 0))


# Procedures

def mask(data: np.ndarray, criterion: tuple = (109, 40, 45), method = similar_color):
    """
    Apply a mask to on pixels with color near of color_tgt
    :param np.ndarray data: Representation of the image to treat
    :param tuple criterion: Color to seek (in RGB)
    :param function method: Method to use for comparaison
    :return: None
    """

    height, width = data.shape[:2]  # Information about the image

    for i in range(height):
        for j in range(width):
            if method(data[i][j], criterion):
                data[i][j] = (0, 0, 0, 255)  # If the color of the pixel is near of colr_tgt, then it becomes dark
            else:
                data[i][j] = (255, 255, 255, 255)  # Else white

        if i % 100 == 0:
            print("MASK", int(i * 10000 / height) / 100, "%")  # Indication about the progression


def clear(data: np.ndarray):
    """
    Erase black pixels with too much white pixels around
    :param np.ndarray data: Representation of the image to treat
    :return: None
    """
    height, width = data.shape[:2]  # Information about the image
    move = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Movements on the four directions

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if data[i][j][0] == 0:  # For each black pixels
                count = 0

                for item in move:  # Count of the number of white pixels around the studied one
                    if data[i + item[0]][j + item[1]][0] == 255:
                        count += 1

                if count >= 3:  # If more than 3 pixels around the studied one, it becomes white
                    data[i][j] = (255, 255, 255, 255)
        if i % 100 == 0:
            print("CLEAR", int(i * 10000 / height) / 100, "%")  # Indication about the progression


def fulfill(data: np.ndarray):
    """
    Fulfill area surrounded by black pixels with black pixels
    :param np.ndarray data: Representation of the image to treat
    :return: None
    """
    height, width = data.shape[:2]  # Information about the image

    for i in range(height):
        for j in range(width):
            if data[i][j][0] == 0:  # For each black pixels
                for k in range(2, 5):  # We look behind the pixel for black pixels and add black pixels between if so
                    if i - k >= 0 and data[i - k][j][0] == 0:  # Horizontally
                        data[i - k + 1][j] = (0, 0, 0, 255)
                    if j - k >= 0 and data[i][j - k][0] == 0:  # Vertically
                        data[i][j- k + 1] = (0, 0, 0, 255)

        if i % 100 == 0:
            print("FULFILL", int(i * 10000 / height) / 100, "%")  # Indication about the progression


def subdivide(array: np.ndarray, sub_height: int, sub_width: int, save_dir: str = "final"):
    """
    Subdivide an image in images of size sub_height x sub_width
    :param np.ndarray array: Representation of the image to treat
    :param int sub_height: Height of subdivision
    :param int sub_width: Width of subdivision
    :param str save_dir: Directory to save the subdivisions
    :return: None
    """
    height, width = array.shape[:2]  # Dimension of the original image

    if height % sub_height != 0 or width % sub_width != 0:
        # If sub_height or sub_width values don't match with the dimension of the image : error
        raise ValueError("Subdivision impossible with given characteristics")
    else:
        x_sub = height // sub_height
        y_sub = width // sub_width

        mkdir(save_dir)  # Creation of the directory for results

        for i in range(x_sub):
            for j in range(y_sub):
                subdivision = [[array[i * sub_height + k][j * sub_width + l] for l in range(sub_height)] for k in range(sub_width)]
                Image.fromarray(np.array(subdivision)).save("{}/subdivision_{}_{}.png".format(save_dir, i, j))

                print("SUBDIVISION {} {}".format(i, j))


def extract(array: np.ndarray):
    """
    Extract information from the treated image
    :param np.ndarray array: Representation of the Image
    :return: Matrix of information
    """
    height, width = array.shape[:2]  # Dimension of the image
    data = np.zeros((height, width))  # Empty array with zeroes

    for i in range(height):
        for j in range(width):
            if array[i][j][0] == 0:  # If the pixel is black, then it is saved as 1
                data[i][j] = 1
            else:  # Else, it is zero
                data[i][j] = 0

    return data
