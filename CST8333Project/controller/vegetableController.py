import datetime
import os
import sys
from time import sleep

from model.vegetablesServices import VegetablesServices
from view.vegetablesView import VegetablesView as View


class VegetableController:
    """
    Controller class for managing vegetable records.

    This class is responsible for controlling the program flow and managing vegetable records. It provides methods for
    initializing the controller, starting the program, displaying the menu, and running each of the menu options.

    Attributes:
        _ALL_VEGETABLES (str): Constant representing the option to view all vegetables.
        _ONE_VEGETABLE (str): Constant representing the option to view one vegetable.
        _ADD_VEGETABLE (str): Constant representing the option to add a vegetable.
        _UPDATE_VEGETABLE (str): Constant representing the option to update a vegetable.
        _DELETE_VEGETABLE (str): Constant representing the option to delete a vegetable.
        _EXTRACT_RECORDS (str): Constant representing the option to extract records to a file.
        _RELOAD_RECORDS (str): Constant representing the option to reload data from a file.
        _EXIT (str): Constant representing the option to exit the program.
    """

    # private variables
    _ALL_VEGETABLES = "1"
    _ONE_VEGETABLE = "2"
    _ADD_VEGETABLE = "3"
    _UPDATE_VEGETABLE = "4"
    _DELETE_VEGETABLE = "5"
    _EXTRACT_RECORDS = "6"
    _RELOAD_RECORDS = "7"
    _VIEW_SORTED = "8"
    _EXIT = "X"

    def __init__(self, database_path: str):
        """
        Initializes the VegetableController object.

        This method initializes the VegetableController object by creating an instance of the VegetablesServices
        class and loading the data to the specified database. If the data cannot be loaded, the program will exit.

        Args:
            database_path (str): The path to the database file with .db extension used by SQLite.

        Returns:
            None
        """

        self.service = VegetablesServices(database_path)
        if not self.service.load_data():
            print("Exiting program")
            sleep(2)
            sys.exit()

    def start(self):
        """
        Starts the program by displaying the menu and controlling the program flow.

        This method displays the menu options to the user and controls the program flow based on the user's input.
        It continues to display the menu and perform the selected actions until the user chooses to exit the program.

        Returns:
            None
        """

        while True:
            View.display_student_name()
            View.display_menu()

            option = View.get_option_input()
            os.system("cls")

            if option == self._ALL_VEGETABLES:
                self.list_all_veges()
            elif option == self._ONE_VEGETABLE:
                self.display_one_veg()
            elif option == self._ADD_VEGETABLE:
                self.add_vegetable()
            elif option == self._UPDATE_VEGETABLE:
                self.update_vegetable()
            elif option == self._DELETE_VEGETABLE:
                self.delete_vegetable()
            elif option == self._EXTRACT_RECORDS:
                self.save_to_file()
            elif option == self._RELOAD_RECORDS:
                self.reload_file()
            elif option == self._VIEW_SORTED:
                self.list_all_sorted()
            elif option.upper() == self._EXIT:
                print("Exiting the program.\n")
                View.display_student_name()
                self.service.db_connection.close()
                sleep(2)
                sys.exit()
            else:
                print("Please enter a correct option value.\n")

    def list_all_veges(self):
        """
        Retrieves all vegetable records from the service and displays them using the view.

        This method retrieves all vegetable records from the `VegetablesServices` instance and converts them to a list of
        records. It then passes the list of records to the `list_all_veges` method of the `View` class to display the
        records in a table format.

        Returns:
            None
        """
        View.display_student_name()

        vegetables = self.service.get_all_vegetables()

        View.list_all_veges(vegetables)

    def display_one_veg(self):
        """
        Retrieves and displays a single vegetable record based on user input.

        This method prompts the user to enter the ID of the vegetable record they want to view. It then retrieves the
        corresponding vegetable record from the `VegetablesServices` instance using the provided ID. If a matching record
        is found, it is displayed using the `display_one_veg` method of the `View` class. The method also provides an
        option to repeat this action if desired.

        Returns:
            None
        """
        View.display_student_name()

        print("\n### VIEW ONE VEGETABLE ###\n")

        id_from_user = View.user_input_veg_id_view()
        vegetable_list = self.service.get_veg_by_id(id_from_user)

        if vegetable_list:
            View.display_one_veg(vegetable_list)
        else:
            print(f"Sorry I didn't find a record with id ({id_from_user})\n")

        if View.is_repeat_operation("view"):
            self.display_one_veg()
        else:
            return

    def add_vegetable(self):
        """
        Adds a new vegetable record to DB Table `vegetable`.

        This method prompts the user to enter the values for each column of the vegetable record using the `add_vegetable`
        method of the `View` class. The entered values are then passed to the `add_vegetable` method of the
        `VegetablesServices` instance to add the new record. After adding the record, the method provides a success/failure
        message and an option to insert another record.

        Returns:
            None
        """
        View.display_student_name()
        print("\n### ADD A VEGETABLE RECORD ###\n")

        vegetable_list = View.add_vegetable()
        self.service.add_vegetable(vegetable_list)
        print("\nVegetable record added successfully.\n")

        if View.is_repeat_operation("add"):
            self.add_vegetable()
        else:
            return

    def update_vegetable(self):
        """
        Updates a vegetable record based on user input.

        This method prompts the user to enter the ID of the record to update using the `user_input_veg_id_view` method
        It then retrieves the corresponding vegetable record from the `VegetablesServices` instance based on the entered
        ID. The user is then prompted to enter the updated values for each column of the record using the
        `update_vegetable` method of the `View` class. The entered values are stored in a list. Finally, the
        `update_vegetable` method of the `VegetablesServices` instance is called to update the record with the new values.

        Returns:
            None
        """
        View.display_student_name()
        print("\n### UPDATE A VEGETABLE RECORD ###\n")

        id_from_user = View.user_input_veg_id_view()
        old_vegetable_obj = self.service.get_veg_by_id(id_from_user)

        if old_vegetable_obj:
            new_vegetable_obj_list = View.update_vegetable(old_vegetable_obj)
            self.service.update_vegetable(new_vegetable_obj_list)
            print("\nVegetable record updated successfully.\n")
        else:
            print(f"Sorry, I didn't find a record with ID {id_from_user}.\n")

        if View.is_repeat_operation("update"):
            self.update_vegetable()
        else:
            return

    def delete_vegetable(self):
        """
        Deletes a vegetable record based on user input.

        This method prompts the user to enter the ID of the record to delete using the `user_input_veg_id_view`.
        It then retrieves the corresponding vegetable record from the `VegetablesServices` instance based on the entered ID.
        If the record exists, it is displayed to the user using the `View.display_one_veg`. The user is then prompted to
        confirm the deletion. If the user confirms the deletion, the `Service.delete_vegetable` method is called to
        delete the record.

        Returns:
            None
        """
        View.display_student_name()
        print("\n### DELETE A VEGETABLE RECORD ###\n")

        id_from_user = View.user_input_veg_id_view()
        vegetable_list = self.service.get_veg_by_id(id_from_user)

        if vegetable_list:
            View.display_one_veg(vegetable_list)
            is_delete = View.delete_vegetable()
            if is_delete:
                self.service.delete_vegetable(id_from_user)
                print("\nThe record is deleted successfully.\n")
        else:
            print(f"Sorry I didn't find a record with id ({id_from_user})\n")

        if View.is_repeat_operation("delete"):
            self.delete_vegetable()
        else:
            return

    def save_to_file(self):
        """
        Saves the vegetable records to a file.

        This method generates a filename based on the current date and time and saves the vegetable records
        to a CSV file with the generated filename. The `View.save_to_file` method is called to show a message of the
        file name, and the `self.service.save_data` method is called to handle the actual file saving process.

        Args:
            self: The current instance of the class.

        Returns:
            None
        """
        View.display_student_name()
        print("\n### SAVE VEGETABLE RECORDS TO FILE ###\n")

        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        file_name = f"vegetable_records_{current_datetime}.csv"

        View.save_to_file(file_name)
        self.service.save_data(file_name)

    def reload_file(self):
        """
        Reloads the data from a file using the associated service.

        This method calls the `load_data` method of the associated service to reload the data from a file.
        If the data is successfully reloaded, a success message is printed.

        Args:
            self: The current instance of the class.

        Returns:
            None
        """
        View.display_student_name()

        if self.service.load_data():
            print("=" * 15)
            print("Data reloaded successfully.")
            print("=" * 15)

    def list_all_sorted(self):
        View.display_student_name()
        print("\n### SORT VEGETABLES BY COLUMNS ###\n")
        sorting_by = View.get_sorting_selection()

        sorted_vegetables = self.service.get_all_vegetables_sorted(sorting_by[0], sorting_by[1])

        View.list_all_veges(sorted_vegetables)

