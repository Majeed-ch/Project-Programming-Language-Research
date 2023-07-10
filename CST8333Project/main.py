from controller.vegetableController import VegetableController


def main():
    """
    Entry point for the program.

    This function serves as the entry point for the program. It initializes a `VegetableController` object `ctrl`
    with the specified `file_path` and calls its `start()` method to begin the program execution.

    Returns:
        None
    """
    db_path = "CST8333_S23.db"
    ctrl = VegetableController(db_path)
    ctrl.start()


if __name__ == "__main__":
    main()
