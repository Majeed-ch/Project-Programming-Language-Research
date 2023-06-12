import datetime
import sys
from time import sleep

from model.vegetablesServices import VegetablesServices
from view.vegetablesView import VegetablesView as View


class VegetableController:
    # private variables
    # TODO: change the names to lowercase with leading _
    __ALL_VEGETABLES = "1"
    __ONE_VEGETABLE = "2"
    __ADD_VEGETABLE = "3"
    __UPDATE_VEGETABLE = "4"
    __DELETE_VEGETABLE = "5"
    __EXTRACT_RECORDS = "6"
    __EXIT = "X"

    def __init__(self, file_path: str):
        self.service = VegetablesServices(file_path)
        if not self.service.load_data():
            print("Exiting program")
            sleep(2)
            sys.exit()

    def start(self):
        """
        Displays the menu and controls the program
        :return:
        """

        while True:
            # os.system('clear')
            View.display_author_name()
            View.display_menu()

            option = View.get_option_input()

            if option == self.__ALL_VEGETABLES:
                self.list_all_veges()
            elif option == self.__ONE_VEGETABLE:
                self.display_one_veg()
            elif option == self.__ADD_VEGETABLE:
                self.add_vegetable()
            elif option == self.__UPDATE_VEGETABLE:
                self.update_vegetable()
            elif option == self.__DELETE_VEGETABLE:
                self.delete_vegetable()
            elif option == self.__EXTRACT_RECORDS:
                self.save_to_file()
            elif option.upper() == self.__EXIT:
                print("Exiting the program.\n")
                View.display_author_name()
                sleep(2)
                sys.exit()
            else:
                print("Please enter a correct option value.\n")

    def list_all_veges(self):
        """
        Show all records to the user
        :return:
        """
        vegetables = []
        for record in self.service.records:
            vegetables.append(record.to_list())

        View.list_all_veges(vegetables)

    def display_one_veg(self):
        """
        Displays a vegetableRecord object based on the id entered by the user
        :return:
        """
        id_from_user = View.user_input_veg_id_view()
        vegetable_obj = self.service.get_veg_by_id(id_from_user)

        if vegetable_obj:
            View.display_one_veg(vegetable_obj)
            if View.is_repeat_operation('view'):
                self.display_one_veg()
            else:
                return
        else:
            print(f"Sorry I didn't find a record with id ({id_from_user})\n")
            if View.is_repeat_operation('view'):
                self.display_one_veg()
            else:
                return

    def add_vegetable(self):
        vegetable_obj = View.add_vegetable()
        self.service.add_vegetable(vegetable_obj)
        # TODO: add a successful/failur message, and an option to insert another record

    def update_vegetable(self):
        # Todo: improve validation (like in display_one_veg())
        id_from_user = View.user_input_veg_id_view()
        old_vegetable_obj = self.service.get_veg_by_id(id_from_user)
        new_vegetable_obj_list = View.update_vegetable(old_vegetable_obj)

        self.service.update_vegetable(old_vegetable_obj, new_vegetable_obj_list)

    def delete_vegetable(self):
        """
        This function deletes a vegetable record based on user input and allows for repeating the operation.
        :return: None.
        """
        id_from_user = View.user_input_veg_id_view()
        vegetable_obj = self.service.get_veg_by_id(id_from_user)

        if vegetable_obj:
            View.display_one_veg(vegetable_obj)
            is_delete = View.delete_vegetable()
            if is_delete:
                self.service.delete_vegetable(vegetable_obj)
                print("The record is deleted successfully.\n")

            if View.is_repeat_operation('delete'):
                self.delete_vegetable()
            else:
                return
        else:
            print(f"Sorry I didn't find a record with id ({id_from_user})\n")
            if View.is_repeat_operation('delete'):
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
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        file_name = f"vegetable_records_{current_datetime}.csv"

        View.save_to_file(file_name)
        self.service.save_data(file_name)
