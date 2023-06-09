import os
import sys
from time import sleep

from model.vegetablesServices import VegetablesServices
from view.vegetablesView import VegetablesView as View


class VegetableController:
    # private variables
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
                print("Implement add record in controller.")
            elif option == self.__UPDATE_VEGETABLE:
                print("Implement update record in controller.")
            elif option == self.__DELETE_VEGETABLE:
                print("Implement delete record in controller.")
            elif option == self.__EXTRACT_RECORDS:
                print("Implement save file in controller.")
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
