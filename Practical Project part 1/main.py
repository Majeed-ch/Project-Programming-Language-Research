import csv
import Dataset32100260DTO as DatasetDTO


def read_csv_file():
    """
    Read the dataset .csv file and parse the data into record objects of Dataset32100260DTO class.

    Returns:
        list: A list of Dataset32100260DTO objects parsed from the .csv file.
    """
    print(f"docstrings: \n{read_csv_file.__doc__}")


def main():
    read_csv_file()


if __name__ == '__main__':
    main()
