import csv
from model.vegetablesRecord import VegetablesRecord


class VegetablesServices:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.records = []

    def load_data(self):
        """
        Loads the dataset to the memory from the csv file.
        :return: True if the loading was successful, False if unsuccessful
        """
        self.records.clear()

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

    @staticmethod
    def save_data(records, new_file_path):
        """
        Saves the in-memory dataset to a new file on the desk.
        :param records: the list of records needs to be saved
        :param new_file_path: the new file name
        :return: None
        """
        try:
            with open(new_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(VegetablesRecord.__dict__.keys())
                for record in records:
                    writer.writerow(record.__dict__.values())
            print("Data saved successfully.")
        except Exception as e:
            print("Error occurred while saving data: ", str(e))

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
