import matplotlib.pyplot as mpl

from fractal_dimension import analyse_one_cell
from map_treatement import prepare
from os import makedirs


def main_script(city: str, year: int, resolution: int, r_max: int, src_dir: str, data_dir: str, result_dir: str,
                show_fig: bool = True):
    """
    Main script of the Analysis, which compile all fractal dimensions in one plot according to the chosen subdivision
    :param str city: Name of the city 
    :param int year: Year of the creation of the used map
    :param int resolution: Subdivision parameter
    :param int r_max: Max size of boxes
    :param str src_dir: Directory of the original image
    :param str data_dir: Directory where temporary data will be saved
    :param str result_dir: Directory where results will be saved
    :param bool show_fig: If a figure should be displayed at the end
    :return: None
    """
    matrix = [[0 for _ in range(resolution)] for _ in range(resolution)]  # Matrix where all fractal dimensions are saved
    data_dir = "{0}/{1}_{2}x{2}".format(data_dir, year, resolution)
    prepare(src_dir, year, resolution, data_dir)  # Application of a mask, then subdivision

    # Computing for all cells
    for i in range(resolution):
        for j in range(resolution):
            print("ANALYSIS", i, j)
            matrix[i][j] = analyse_one_cell("{0}/subdivision_{1}_{2}.png".format(data_dir, i, j), r_max)

    makedirs(result_dir, exist_ok=True)

    # Saving of the fractal dimensions in a csv file
    with open("{}/{}_{}.csv".format(result_dir, city, year), 'a') as file:
        file.write("X,Y,Fractal Dimension\n")

        for i in range(resolution):
            for j in range(resolution):
                file.write("{},{},{}\n".format(i, j, matrix[i][j]))

    mpl.close()
    mpl.imshow(matrix, cmap="Spectral", vmin=-2, vmax=2)  # Plot to show all the fractal dimensions
    mpl.title("{} {}".format(city, year))
    mpl.colorbar()

    mpl.savefig("{}/{}_{}".format(result_dir, city, year), dpi=300)  # Saving of the figure

    if show_fig:
        mpl.show()
