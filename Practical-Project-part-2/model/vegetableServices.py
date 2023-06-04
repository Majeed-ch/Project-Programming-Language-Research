import csv
from vegetablesRecord import VegetablesRecord


class VegetablesServices:
    def __int__(self, file_path: str):
        self.file_path = file_path
        self.records = []
        self.load_data()

    def load_data(self):
        """
        Loads the dataset to the memory from the csv file.
        :return:
        List of vegetablesRecord objects
        """
        print("loading records...")
        try:
            with open(self.file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)

                # Skip the first row (header row)
                next(reader)

                # Parse the first 100 records in the file
                rows_counter = 0
                for row in reader:
                    rows_counter += 1
                    # record = DatasetDTO.DatasetS23(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    #                                row[8],
                    #                                row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                    # records.append(record.to_list())
                    record = VegetablesRecord(*row)
                    self.records.append(record)
                    if rows_counter == 100:
                        break

        except FileNotFoundError:
            print(f"File ${self.file_path} not found.")
        except IOError:
            print(f"Error reading file ${self.file_path}.")
