from tabulate import tabulate


class VegetablesView:
    _vegetable_fields = [
        "REF_DATE",
        "GEO",
        "DGUID",
        "Type of product",
        "Type of storage",
        "UOM",
        "UOM_ID",
        "SCALAR_FACTOR",
        "SCALAR_ID",
        "VECTOR",
        "COORDINATE",
        "VALUE",
        "STATUS",
        "SYMBOL",
        "TERMINATED",
        "DECIMALS",
    ]

    @staticmethod
    def display_menu():
        """
        Displays the options menu.

        This static method displays an options menu with various menu items using the `tabulate` function from
        the `tabulate` library.

        Returns:
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
            ["(7)", "Reload data from file"],
            ["(X)", "Exit"],
        ]

        print(tabulate(menu, tablefmt="fancy_grid"))

    @staticmethod
    def get_option_input():
        """
        Retrieves the user's option input.

        Prompts the user to enter their option choice from the menu.

        Returns:
            str: The user's option input.
        """
        return input("\nChoose an option from the menu: ")

    @staticmethod
    def list_all_veges(vegetables):
        """
        Lists all the vegetables in a table format, with a header row.


        Args:
            vegetables (list): A list of vegetables to display in the table.

        Returns:
            None
        """

        print(tabulate(vegetables, headers=VegetablesView._vegetable_fields, tablefmt="simple_outline"))

    @staticmethod
    def display_one_veg(vegetable):
        """
        Displays the details of a single vegetable.

        This static method takes a single vegetable `vegetable` and displays its details in a tabular format.

        Args:
            vegetable (VegetablesRecord): The vegetable object to display its details.

        Returns:
            None
        """
        veg_details = [
            ["ID", vegetable.veg_id],
            ["REF_DATE", vegetable.ref_date],
            ["GEO", vegetable.geo],
            ["DGUID", vegetable.dguid],
            ["Type of product", vegetable.type_of_product],
            ["Type of storage", vegetable.type_of_storage],
            ["UOM", vegetable.uom],
            ["UOM_ID", vegetable.uom_id],
            ["SCALAR_FACTOR", vegetable.scalar_factor],
            ["SCALAR_ID", vegetable.scalar_id],
            ["VECTOR", vegetable.vector],
            ["COORDINATE", vegetable.coordinate],
            ["VALUE", vegetable.value],
            ["STATUS", vegetable.status],
            ["SYMBOL", vegetable.symbol],
            ["TERMINATED", vegetable.terminated],
            ["DECIMALS", vegetable.decimals],
        ]

        print(tabulate(veg_details, tablefmt="simple"))

    @staticmethod
    def add_vegetable():
        """
        Prompts the user to enter the values for each column of a vegetable record.

        It iterates through each column in the `VegetablesView._vegetable_fields` list and asks the user to input a
        value for that column. The entered values are stored in a list `record` and returned.

        Returns:
            list: A list containing the values for each column of the vegetable record.
        """
        record = []

        print("Please enter the values for each of the columns: ")
        for column in VegetablesView._vegetable_fields:
            value = input(f"{column}: ")
            record.append(value)

        return record

    @staticmethod
    def update_vegetable(vegetable):
        """
        prompts the user to update the values of each column in a vegetable record, and appends the record ID to the end
        of the list.

        Args:
            vegetable (VegetablesRecord): The existing vegetable object to be updated.

        Returns:
            list: A list containing the updated values for each column of the vegetable record and its ID.
        """
        old_vegetable_list = vegetable.to_list()
        veg_id = old_vegetable_list.pop(0)  # removing the id

        new_vegetable_list = []

        print("=" * 10)
        print(
            "Enter the value of each column to update it\n"
            "Leave it empty if no need to update"
        )
        print("=" * 10)

        for column, old_value in zip(
            VegetablesView._vegetable_fields, old_vegetable_list
        ):
            new_value = input(f"{column}: {old_value} <- ")

            if new_value:
                new_vegetable_list.append(new_value)
            else:
                new_vegetable_list.append(old_value)

        new_vegetable_list.append(veg_id)  # adding the id to the end of the list
        return new_vegetable_list

    @staticmethod
    def delete_vegetable():
        """
        Prompts the user for confirmation to delete a record.

        This function continuously asks the user for confirmation until a valid input
        of 'yes' or 'no' is provided. The function returns a boolean value based on
        the user's choice.

        Returns:
            bool: True if the user confirms deletion, False if cancellation is requested.
        """
        while True:
            response = (
                input("\nAre you sure want to delete this record? (y/n) ")
                .strip()
                .lower()
            )
            if response in ["yes", "y"]:
                return True
            elif response in ["no", "n"]:
                print("\nCanceling...")
                return False
            else:
                print("Invalid input. Please enter yes or no.")
                print("=" * 10, end="\n")

    @staticmethod
    def save_to_file(file_name):
        """
        Saves a file with the given filename.

        This static method prints a message indicating the filename being saved.

        Args:
            file_name (str): The name of the file to be saved.

        Returns:
            None
        """

        print(f"saving file as {file_name}\n")

    @staticmethod
    def user_input_veg_id_view():
        """
        Prompts the user to input a vegetable ID.

        This static method prompts the user to enter the ID of a vegetable record.
        It repeatedly asks for user input until a valid integer ID is provided.
        If the user enters a non-numeric value, an error message is displayed, and the user is asked to input again.

        Returns:
            int: The user-input vegetable ID.
        """
        while True:
            try:
                input_veg_id = int(input("Please enter the ID of the record: "))
                return input_veg_id
            except ValueError:
                print(
                    "Invalid input. Please check your input, it should be a number.\n"
                )

    @staticmethod
    def is_repeat_operation(action: str) -> bool:
        """
        Asks the user if they want to repeat a certain action.

        Prompts the user with a message asking if they want to repeat a specific action. The action
        is specified by the `action` parameter. The method returns True if the user wants to repeat the action
        and False otherwise. It keeps asking for input until a valid response is provided.

        Args:
            action (str): The action for which the user is being prompted to repeat.

        Returns:
            bool: True if the user wants to repeat the action, False otherwise.
        """
        while True:
            response = (
                input(f"Do you want to {action} another record? (y/n) ").strip().lower()
            )
            print(" ")
            if response in ["yes", "y"]:
                return True
            elif response in ["no", "n"]:
                return False
            else:
                print("Invalid input. Please enter yes or no.")
                print("=" * 10, end="\n")

    @staticmethod
    def display_student_name():
        """
        Displays the name of the student (Abdul Mazed) in a box.

        Returns:
            None
        """
        print("\n" + tabulate([["Program created by Abdul Mazed"]], tablefmt="outline"))
