import csv
import sqlite3
from sqlite3 import DatabaseError

from model.vegetablesRecord import VegetablesRecord


class VegetablesServices:
    def __init__(self, database_path: str):
        self.db_path = database_path
        self.db_connection = sqlite3.connect(database_path)
        self.db_connection.row_factory = self.list_factory
        self.cursor = self.db_connection.cursor()

    def load_data(self):
        """
        Using the SQL script provided, it creates a vegetable table in the database and populates is with data.

        Args:
            self: The current instance of the class.

        Returns:
            bool: True if the SQL file is successfully loaded, False otherwise.
        """
        sql_file = "vegetables.sql"
        try:
            with open(sql_file, "r") as file:
                sql_script = file.read()

            with self.db_connection:
                self.cursor.executescript(sql_script)
            return True

        except FileNotFoundError:
            print(f"File {sql_file} not found.")
            return False
        except IOError:
            print(f"Error reading file {sql_file}.")
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
            "id",
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

        records_list = self.cursor.execute("SELECT * FROM vegetable;").fetchall()

        try:
            with open(new_file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(field_names)
                for record in records_list:
                    writer.writerow([record[field_names.index(field)] for field in field_names])
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
            list / None: The vegetable record list if found, None otherwise.
        """
        self.cursor.execute("SELECT * FROM vegetable WHERE id = :id;", {"id": veg_id})

        row = self.cursor.fetchone()
        if row:
            return row

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

    def update_vegetable(self, new_record_list):
        """
        Updates the attributes of an existing vegetable record in the database.

        Args:
            self: The current instance of the class.
            new_record_list (list): A list containing the updated attribute values for the record, and contains the
            vegetable record id as the last element.

        Returns:
            None
        """
        with self.db_connection:
            self.cursor.execute("UPDATE vegetable SET ref_date=?, geo=?, dguid=?, type_of_product=?, type_of_storage=?,"
                                "uom=?, uom_id=?, scalar_factor=?, scalar_id=?, vector=?, coordinate=?, value=?, "
                                "status =?, symbol=?, terminated=?, decimals=?"
                                "WHERE id = ?;", new_record_list)

    def delete_vegetable(self, veg_id):
        """
        Removes a vegetable record from the list of records.

        Args:
            self: The current instance of the class.
            veg_id (int): The ID of the vegetable record to be deleted.

        Returns:
            None
        """
        with self.db_connection:
            self.cursor.execute("DELETE FROM vegetable WHERE id = :vegetable_id", {"vegetable_id": veg_id})

    @staticmethod
    def list_factory(cursor, row):
        """
        Custom row factory function that converts each row into a list.

        This function is designed to be used as the row_factory for a SQLite connection or cursor object.
        It takes two arguments: `cursor` and `row` which typically provided by the connection not the user.

        Parameters:
            cursor (sqlite3.Cursor): The SQLite cursor object.
            row (tuple): A row retrieved from the database query result.

        Returns:
            list: The row converted into a list.
        """
        return list(row)
