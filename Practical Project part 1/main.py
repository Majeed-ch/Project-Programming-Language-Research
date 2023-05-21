import csv
import Dataset32100260DTO as DatasetDTO

# tabulate package is needed to print the table, if it's not available we print as plain text instead
try:
    from tabulate import tabulate

    tabulate_available = True

except ImportError:
    tabulate_available = False


def read_csv_file():
    """
    Read the dataset .csv file and parse the data into record objects of DatasetS23 class.

    Returns:
        list: A list of Dataset32100260DTO objects parsed from the .csv file.
    """
    records = []

    print("reading the csv file and parsing the first 5 records...")

    try:
        with open('32100260.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            # Skip the first row (header row)
            next(reader)

            # Parse the first 5 records in the file
            rows_counter = 0
            for row in reader:
                rows_counter += 1
                record = DatasetDTO.DatasetS23(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                               row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                records.append(record.to_list())
                if rows_counter == 5:
                    break

    except FileNotFoundError:
        print("File 32100260.csv not found.")
    except IOError:
        print("Error reading file 32100260.csv.")

    return records


def main():
    print("==================")
    print("Abdul Mazed \nStudent# 041037830 \nCST8333_350_Practical_project_part1")
    print("==================")

    # a list of records returned from reding the csv file
    dataset = read_csv_file()

    record: DatasetDTO.DatasetS23

    print("printing the parsed records...")

    header_row = ["REF_DATE", "GEO", "DGUID", "Type of product", "Type of storage", "UOM", "UOM_ID", "SCALAR_FACTOR",
                  "SCALAR_ID", "VECTOR", "COORDINATE", "VALUE", "STATUS", "SYMBOL", "TERMINATED", "DECIMALS"]

    print(tabulate(dataset, headers=header_row, tablefmt="grid"))


if __name__ == '__main__':
    main()
