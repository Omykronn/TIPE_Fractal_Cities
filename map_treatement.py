import math


def distance_euclid(v1: tuple, v2: tuple):
    """
    Distance associated to the euclidian norm in R³

    :param tuple v1: 3-tuple n°1
    :param tuple v2: 3-tuple n°2
    :return float: Distance between vector1 and vector2
    """
    return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2 + (v1[2] - v2[2]) ** 2)


def mask(data, color_tgt: tuple = (109, 40, 45), precision: float = 27):
    """
    Apply a mask to on pixels with color near of color_tgt

    :param data: Representation of the image to treat
    :param tuple color_tgt: Color to seek (in RGB)
    :param int precision: Index of precision
    :return: None
    """

    height, width = data.shape[:2]  # Information about the image

    for i in range(height):
        for j in range(width):
            if distance_euclid(color_tgt, data[i][j]) <= precision:
                data[i][j] = (0, 0, 0)  # If the color of the pixel is near of colr_tgt, then it becomes dark
            else:
                data[i][j] = (255, 255, 255)  # Else white

        if i % 100 == 0:
            print("MASK", int(i * 10000 / height) / 100, "%")  # Indication about the progression


def clear(data):
    """
    Erase black pixels with too much white pixels around

    :param data: Representation of the image to treat
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
                    data[i][j] = (255, 255, 255)
        if i % 100 == 0:
            print("CLEAR", int(i * 10000 / height) / 100, "%")  # Indication about the progression


def fulfill(data):
    """
    Fulfill area surrounded by black pixels with black pixels

    :param data: Representation of the image to treat
    :return: None
    """
    height, width = data.shape[:2]  # Information about the image

    for i in range(height):
        for j in range(width):
            if data[i][j][0] == 0:  # For each black pixels
                for k in range(2, 5):  # We look behind the pixel for black pixels and add black pixels between if so
                    if i - k >= 0 and data[i - k][j][0] == 0:  # Horizontally
                        data[i - k + 1][j] = (0, 0, 0)
                    if j - k >= 0 and data[i][j - k][0] == 0:  # Vertically
                        data[i][j- k + 1] = (0, 0, 0)

        if i % 100 == 0:
            print("FULFILL", int(i * 10000 / height) / 100, "%")  # Indication about the progression
