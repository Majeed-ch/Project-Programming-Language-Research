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

    def start(self):
        """
        Displays the menu and controls the program
        :return:
        """

        while True:
            os.system('clear')
            View.display_author_name()
            View.display_menu()

            option = View.get_option_input()

            if option == self.__ALL_VEGETABLES:
                print("Implement show all in controller.")
            elif option == self.__ONE_VEGETABLE:
                print("Implement show one in controller.")
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
                input("Please enter a correct option value.")

