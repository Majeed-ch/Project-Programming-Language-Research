from controller.vegetableController import VegetableController


def main():
    """
    Entry point of the application
    :return:
    """
    file_path = "32100260.csv"
    ctrl = VegetableController(file_path)
    ctrl.start()


if __name__ == '__main__':
    main()
