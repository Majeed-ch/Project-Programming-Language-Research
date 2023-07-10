import csv
import sqlite3
from sqlite3 import DatabaseError

from model.vegetablesRecord import VegetablesRecord


class VegetablesServices:
    def __init__(self, database_path: str):
        self.db_path = database_path
        self.db_connection = sqlite3.connect(database_path)
        self.cursor = self.db_connection.cursor()
        self.records = []

    def load_data(self):
        """
        Using the SQL script provided, it creates a vegetable table in the database and populates is with data.

        Args:
            self: The current instance of the class.

        Returns:
            bool: True if the SQL file is successfully loaded, False otherwise.
        """
        self.records.clear()

        try:
            with open("vegetables.sql", "r") as file:
                sql_script = file.read()

            with self.db_connection:
                self.cursor.executescript(sql_script)
            return True

        except FileNotFoundError:
            print("File vegetables.sql not found.")
            return False
        except IOError:
            print("Error reading file vegetables.sql.")
            return False
        except DatabaseError as ex:
            print(f"Error happened working with the database: {ex}")

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
        field_names = [
            "ref_date",
            "geo",
            "dguid",
            "type_of_product",
            "type_of_storage",
            "uom",
            "uom_id",
            "scalar_factor",
            "scalar_id",
            "vector",
            "coordinate",
            "value",
            "status",
            "symbol",
            "terminated",
            "decimals",
        ]

        try:
            with open(new_file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(field_names)
                for record in self.records:
                    writer.writerow([getattr(record, field) for field in field_names])
            print("Data saved successfully.\n")
        except Exception as e:
            print("Error occurred while saving data: \n", str(e))

    def get_all_vegetables(self):
        """
        Returns all the vegetable records stored in the DB Table `vegetable`.

        Args:
            self: The current instance of the class.

        Returns:
            list: A list containing all the vegetable records.
        """

        result = self.cursor.execute("SELECT * FROM vegetable;")
        return result.fetchall()

    def get_veg_by_id(self, veg_id):
        """
        Retrieves one record from the DB Table `vegetable` based on the passed id

        Args:
            self: The current instance of the class.
            veg_id (int): The ID of the vegetable record to search for.

        Returns:
            VegetablesRecord / None: The vegetable record if found, None otherwise.
        """
        self.cursor.execute("SELECT * FROM vegetable WHERE id = :id;", {"id": veg_id})

        row = self.cursor.fetchone()
        if row:
            return VegetablesRecord.from_iterable(row)

        return None

    def add_vegetable(self, record):
        """
        Adds a vegetable record to the DB Table `vegetable`.

        Args:
            self: The current instance of the class.
            record (list): A list containing the attribute values for the vegetable record.

        Returns:
            None
        """
        with self.db_connection:
            self.cursor.execute("INSERT INTO vegetable(ref_date, geo, dguid, type_of_product, type_of_storage,"
                                " uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol,"
                                " terminated, decimals) "
                                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", record)

    @staticmethod
    def update_vegetable(old_record, new_record_list):
        """
        Updates the attributes of an existing vegetable record.

        This static method takes an existing `VegetablesRecord` object `old_record` and a list `new_record_list`
        containing the updated attribute values. The method assigns each element of `new_record_list` to the
        corresponding attribute of `old_record` to update its values.

        Args:
            old_record (VegetablesRecord): The existing vegetable record object to update.
            new_record_list (list): A list containing the updated attribute values for the record.

        Returns:
            None
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
