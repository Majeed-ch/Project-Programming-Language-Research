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

    def update_vegetable(self, old_record, new_record):
        """
        Updates the list of records with the passed record
        :param old_record: The vegetableRecord object that needs to be updated
        :param new_record: The updated vegetableRecord object
        :return:
        """
        index = self.records.index(old_record)
        self.records[index] = new_record

    def delete_vegetable(self, veg_id):
        """
        Deletes a record from the list of records
        :param veg_id: The id of the object that needs to be deleted
        :return:
        """
        record = self._search_list(veg_id)
        if record is not None:
            response = input(f"are you sure you want to delete this record?(y/n)\n"
                             f"{record.__str__()}")
            if response[0].lower() == 'y':
                self.records.remove(record)
            else:
                print('canceling deletion')
                return
        else:
            print("There was an error deleting the record")

    def _search_list(self, veg_id):
        """
        Searches the list of records for the object with the id equals the passed id
        :param veg_id: the id of the requested record
        :return: VegetablesRecord object or None if not found
        """
        for record in self.records:
            if record.veg_id == veg_id:
                return record
            else:
                return None
