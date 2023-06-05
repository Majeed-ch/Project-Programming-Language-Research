from controller.vegetableController import VegetableController


def main():
    file_path = "32100260.csv"
    ctrl = VegetableController(file_path)
    ctrl.start()


if __name__ == '__main__':
    main()
