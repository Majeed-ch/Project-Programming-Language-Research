from tabulate import tabulate


class VegetablesView:

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

        # for column in header_row:
        #     print(column, end=' | ')
        #
        # for row in vegetables:
        #     print("")
        #     for column in row:
        #         print(column, end=' | ')

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
    def add_veg():
        """
        Interacts with the user to set values of one record then adds it to the records in-memory.
        :return:
        None
        """
        pass
        # TODO: Create an object and get inputs from the user for each record member then pass it to the controller to
        #  insert it in-memory.

    @staticmethod
    def update_veg():
        """
        Get user inputs to update a record based on the record id entered by the user.
        :return:
        None
        """
        pass
        # TODO: Get the id from the user, get the corresponding record from the controller, inputs from the user for
        #  each record member then pass the record to the controller to update the record in-memory.

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

        :return: The id of the vegetable record
        """
        while True:
            try:
                input_veg_id = int(input("Please enter the ID of the record: "))
                return input_veg_id
            except ValueError:
                print("Invalid input. Please check your input, it should be a number\n.")

    @staticmethod
    def display_author_name():
        print("__Program created by Abdul Mazed__")
