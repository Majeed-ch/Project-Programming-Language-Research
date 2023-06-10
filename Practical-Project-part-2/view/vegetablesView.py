from tabulate import tabulate


class VegetablesView:

    _vegetable_fields = ["REF_DATE", "GEO", "DGUID", "Type of product", "Type of storage", "UOM", "UOM_ID",
                         "SCALAR_FACTOR", "SCALAR_ID", "VECTOR", "COORDINATE", "VALUE", "STATUS", "SYMBOL",
                         "TERMINATED", "DECIMALS"]
    @staticmethod
    def display_menu():
        """
        Prints out on the console a menu of options for managing vegetables dataset
        :return:
        None
        """
        menu = [
            ["", "Abdul Mazed"],
            ["", "Options Menu"],
            ["(1)", "View all vegetables"],
            ["(2)", "View one vegetable"],
            ["(3)", "Add vegetable"],
            ["(4)", "Update vegetable"],
            ["(5)", "Delete vegetable"],
            ["(6)", "Extract records to a file"],
            ["(X)", "Exit"],
        ]

        print(tabulate(menu, tablefmt="fancy_grid"))

    @staticmethod
    def get_option_input():
        """
        Asks user to select an option from the menu
        :return: The selected option number/letter
        """
        return input('\nChoose an option from the menu: ')

    @staticmethod
    def list_all_veges(vegetables):
        """
        prints out on the console a list of the first 100 records in the dataset,
        and prints student name every 10 records
        :return:
        None
        """
        #TODO: print the passed list in a table (like in project 1).
        header_row = ["ID", "REF_DATE", "GEO", "DGUID", "Type of product", "Type of storage", "UOM", "UOM_ID",
                      "SCALAR_FACTOR",
                      "SCALAR_ID", "VECTOR", "COORDINATE", "VALUE", "STATUS", "SYMBOL", "TERMINATED", "DECIMALS"]

        print(tabulate(vegetables, headers=header_row, tablefmt="fancy_grid"))

    @staticmethod
    def display_one_veg(vegetable):
        """
        Prints out the details of the passed vegetableRecord object
        :return:
        """
        # TODO: Get user input for the record id, get the record form a controller method then print it.
        veg_details = [
            ['ID', vegetable.veg_id],
            ['REF_DATE', vegetable.ref_date],
            ['GEO', vegetable.geo],
            ['DGUID', vegetable.dguid],
            ['Type of product', vegetable.type_of_product],
            ['Type of storage', vegetable.type_of_storage],
            ['UOM', vegetable.uom],
            ['UOM_ID', vegetable.uom_id],
            ['SCALAR_FACTOR', vegetable.scalar_factor],
            ['SCALAR_ID', vegetable.scalar_id],
            ['VECTOR', vegetable.vector],
            ['COORDINATE', vegetable.coordinate],
            ['VALUE', vegetable.value],
            ['STATUS', vegetable.status],
            ['SYMBOL', vegetable.symbol],
            ['TERMINATED', vegetable.terminated],
            ['DECIMALS', vegetable.decimals]
        ]

        print(tabulate(veg_details, tablefmt='simple'))

    @staticmethod
    def add_vegetable():
        """
        Interacts with the user to set values of one record to be added to the list of records in-memory.
        :return: A list of vegetableRecord attributes values to be inserted/added.
        """
        # TODO: Create an object and get inputs from the user for each record member then pass it to the controller to
        #  insert it in-memory.
        record = []

        print("Please enter the values for each of the columns: ")
        for column in VegetablesView._vegetable_fields:
            value = input(f"{column}: ")
            record.append(value)

        return record

    @staticmethod
    def update_vegetable(vegetable):
        """
        Gets user inputs to update the vegetableRecord passed to the method.
        :param vegetable: The VegetableRecord object to be updated
        :return:
        """
        # TODO: Get the id from the user, get the corresponding record from the controller, inputs from the user for
        #  each record member then pass the record to the controller to update the record in-memory.
        old_vegetable_list = vegetable.to_list()
        old_vegetable_list.pop(0)  # removing the id

        new_vegetable_list = []

        print("="*10)
        print("Enter the value of each column to update it\n"
              "Leave it empty if no need to update")
        print("=" * 10)

        for column, old_value in zip(VegetablesView._vegetable_fields, old_vegetable_list):
            new_value = input(f"{column}: {old_value} <- ")

            if new_value:
                new_vegetable_list.append(new_value)
            else:
                new_vegetable_list.append(old_value)

        return new_vegetable_list

    @staticmethod
    def delete_veg():
        """
        Deletes a record from the in-memory records based on the id entered by the user, a conformation message is shown
        before processing the deletion.
        :return:
        None
        """
        pass
        # TODO: ask for id, pass it to the controller to delete it.

    @staticmethod
    def save_file_view():
        """
        Prints a message for processing the file saving and a message after it finished.
        :return:
        None
        """
        pass
        # TODO: Show a message that file is saving, call save_file method from controller, show done or fail message.

    @staticmethod
    def user_input_veg_id_view():
        """
        Asks the user for the id of the vegetable record
        :return: The id of the vegetable record
        """
        while True:
            try:
                input_veg_id = int(input("Please enter the ID of the record: "))
                return input_veg_id
            except ValueError:
                print("Invalid input. Please check your input, it should be a number.\n")

    @staticmethod
    def is_repeat_operation(action: str) -> bool:
        """
        Asks user if they wish to repeat the same operation they were using,
        so they do not need to go to the menu again
        :param action: The action being performed
        :return: True if the user wants to repeat, False otherwise
        """
        while True:
            response = input(f"Do you want to {action} another record? (y/n) ").lower()
            print(" ")
            if response[0] == 'y':
                return True
            elif response[0] == 'n':
                return False
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
                print("=" * 10, end="\n")

    @staticmethod
    def display_author_name():
        print("__Program created by Abdul Mazed__")
