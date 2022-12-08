import numpy as np
import math
from PIL import Image

dir_file = "example.png"  # Image to treat
color_tgt = (123, 61, 59)  # Color to find
precision = 27  # Error that is accepted (here 27 seems to be the best)


def distance_euclid(vector1, vector2):
    """
    Distance associated to the euclidian norm in R³

    :param vector1: 3-uplet n°1
    :param vector2: 3-uplet n°2
    :return float: Distance between vector1 and vector2
    """
    s = 0

    for k in range(3):
        s += (vector1[k] - vector2[k]) ** 2

    return math.sqrt(s)


array = np.array(Image.open("sample_grenoble_1866.jpg")).copy()  # Extraction of the image into an array with PIL
height, width = array.shape[:2]  # Information about the image

for i in range(height):
    for j in range(width):
        if distance_euclid(color_tgt, array[i][j]) <= precision:
            array[i][j] = (0, 0, 0)  # If the color of the pixel is near of colr_tgt, then it becomes white
        else:
            array[i][j] = (255, 255, 255)  # Else dark

    if i % 100 == 0:
        print(int(i * 10000 / height) / 100, "% DONE")  # Indication about the progression

Image.fromarray(array).save(dir_file[:-4] + "_treated" + dir_file[-4:])  # Exportation of the treated image
