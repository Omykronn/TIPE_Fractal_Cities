import math
import numpy as np

from PIL import Image
from os import makedirs


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
            
    print("MASK DONE")


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
                        data[i][j - k + 1] = (0, 0, 0, 255)

        if i % 100 == 0:
            print("FULFILL", int(i * 10000 / height) / 100, "%")  # Indication about the progression


def subdivide(array: np.ndarray, x_sub: int, y_sub: int, dilatation: int, save_dir: str = "final"):
    """
    Subdivide an image in little images
    :param np.ndarray array: Representation of the image to treat
    :param int x_sub: Number of subdivisions on the x-axis
    :param int y_sub: Number of subdivisions on the y-axis
    :param int dilatation: Dilatation Factor of subdivisons
    :param str save_dir: Directory to save the subdivisions
    :return: None
    """
    height, width = array.shape[:2]  # Dimension of the original image

    if height % x_sub != 0 or width % y_sub != 0:
        # If sub_height or sub_width values don't match with the dimension of the image : error
        raise ValueError("Subdivision impossible with given characteristics")
    else:
        new_height = height // x_sub
        new_width = width // y_sub
        
        print(new_height, new_width)

        makedirs(save_dir, exist_ok=True)  # Creation of the directory for results

        for i in range(x_sub):
            for j in range(y_sub):
                subdivision = [[array[i * new_height + k][j * new_width + l] for l in range(new_width)] for k in range(new_height)]
                #subdivision = dilate(subdivision, dilatation)
                Image.fromarray(np.array(subdivision)).save("{}/subdivision_{}_{}.png".format(save_dir, i, j))

                print("SUBDIVISION {} {}".format(i, j))


def extract(array: np.ndarray):
    """
    Extract information from the treated image
    :param np.ndarray array: Representation of the Image
    :return np.ndarray * bool: Matrix of information
    """
    height, width = array.shape[:2]  # Dimension of the image
    data = np.zeros((height, width))  # Empty array with zeroes

    empty = True  # Check if the picture is not empty

    for i in range(height):
        for j in range(width):
            if array[i][j][0] == 0:  # If the pixel is black, then it is saved as 1
                data[i][j] = 1
                empty = False

    return data, empty


def prepare(name_file: str, resolution: int, dilatation: int, exit_dir: str = "data"):
    """
    Prepare files from an image for the fractal analysis
    :param str name_file: File's name
    :param int resolution: Root of the number of sub-images to create
    :param int dilatation: Factor of dilatation of subdivisions
    :param str exit_dir: Directory where all the files will be created (default : data)
    :return: None
    """
    picture = np.array(Image.open(name_file))  # Open the image

    # Creation of all the needed directory
    makedirs(exit_dir, exist_ok=True)

    mask(picture, (200, 200, 200), darker_color)  # First : application of a mask to keep only the useful data (for CORINE : 16)
    subdivide(picture, resolution, resolution, dilatation, exit_dir)  # Then, subdivision of the image according to resolution


def dilate(array: list, factor: int):
    """
    :param list array: Image to dilate
    :param int factor: Factor of dilatation
    :return np.ndarray result: Dilated Image
    """
    assert type(factor) is int

    height, width = len(array), len(array[0])  # TODO : Prendre en compte si la matrice est totalement vide

    result = [[0 for _ in range(width * factor)] for _ in range(height * factor)]

    for i in range(height):
        for j in range(width):
            # Copy of one pixel 
            for k in range(factor):
                for l in range(factor):
                    result[i * factor + k][j * factor + l] = array[i][j] 

    return np.array(result)
