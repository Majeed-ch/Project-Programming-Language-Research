import csv
from model.vegetablesRecord import VegetablesRecord


class VegetablesServices:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.records = []

    def load_data(self):
        """
            Loads data from a file into the records list.

            This method clears the current records list and resets the last ID of the `VegetablesRecord` class.
            It then attempts to load data from the file specified by `self.file_path`. The file is read using the
            `csv.reader` module, skipping the first row (header row) and parsing the next 100 rows as records.
            Each row is converted into a `VegetablesRecord` object using the `from_list` method and added to the
            records list. If the file is successfully loaded, the method returns True; otherwise, it returns False
            and prints an appropriate error message.

            Args:
                self: The current instance of the class.

            Returns:
                bool: True if the file is successfully loaded, False otherwise.
            """
        self.records.clear()
        VegetablesRecord._last_id = 0

        try:
            with open(self.file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)

                # Skip the first row (header row)
                next(reader)

                # Parse the first 100 records in the file
                rows_counter = 0
                for row in reader:
                    rows_counter += 1
                    record = VegetablesRecord.from_list(row)
                    self.records.append(record)
                    if rows_counter == 100:
                        break

                return True

        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return False
        except IOError:
            print(f"Error reading file {self.file_path}.")
            return False

    def save_data(self, new_file_path):
        """
        Saves the data to a CSV file.

        This method saves the data from the `self.records` list to a CSV file specified by `new_file_path`.
        The field names for the CSV columns are defined in `field_names` list. Each record's attributes
        corresponding to the field names are written to the file using the `csv.writer` module.

        Args:
            self: The current instance of the class.
            new_file_path (str): The path of the new CSV file to be created and saved.

        Returns:
            None
        """
        field_names = ["ref_date", "geo", "dguid", "type_of_product", "type_of_storage", "uom", "uom_id",
                       "scalar_factor", "scalar_id", "vector", "coordinate", "value", "status", "symbol",
                       "terminated", "decimals"]

        try:
            with open(new_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(field_names)
                for record in self.records:
                    writer.writerow([getattr(record, field) for field in field_names])
            print("Data saved successfully.\n")
        except Exception as e:
            print("Error occurred while saving data: \n", str(e))

    def get_all_vegetables(self):
        """
        Retrieves all the records that was loaded form the file.
        :return: List of VegetablesRecord objects
        """
        return self.records

    def get_veg_by_id(self, veg_id):
        """
        Retrieves one record from the list based on the passed id
        :param veg_id: the id of the requested record
        :return: VegetablesRecord object or None if not found
        """
        return self._search_list(veg_id)

    def add_vegetable(self, record):
        """
        Adds a new record to the list of vegetableRecords
        :param record: A list of vegetableRecord attributes values
        :return:
        """
        vegetable_obj = VegetablesRecord.from_list(record)
        self.records.append(vegetable_obj)

    def update_vegetable(self, old_record, new_record_list):
        """
        Updates the list of records with the passed record
        :param old_record: The vegetableRecord object that needs to be updated
        :param new_record_list: The updated vegetableRecord object
        :return:
        """
        old_record.ref_date = new_record_list[0]
        old_record.geo = new_record_list[1]
        old_record.dguid = new_record_list[2]
        old_record.type_of_product = new_record_list[3]
        old_record.type_of_storage = new_record_list[4]
        old_record.uom = new_record_list[5]
        old_record.uom_id = new_record_list[6]
        old_record.scalar_factor = new_record_list[7]
        old_record.scalar_id = new_record_list[8]
        old_record.vector = new_record_list[9]
        old_record.coordinate = new_record_list[10]
        old_record.value = new_record_list[11]
        old_record.status = new_record_list[12]
        old_record.symbol = new_record_list[13]
        old_record.terminated = new_record_list[14]
        old_record.decimals = new_record_list[15]

    def delete_vegetable(self, vegetable):
        """
        Removes a vegetable record from the list of records.

        This method removes the specified `vegetable` from the `records` list.

        Args:
            self: The current instance of the class.
            vegetable: The vegetable record to be deleted.

        Returns:
            None
        """
        self.records.remove(vegetable)

    def _search_list(self, veg_id):
        """
        Searches the list of records for the object with the id equals the passed id
        :param veg_id: the id of the requested record
        :return: VegetablesRecord object or None if not found
        """
        for record in self.records:
            if record.veg_id == veg_id:
                return record

        return None
