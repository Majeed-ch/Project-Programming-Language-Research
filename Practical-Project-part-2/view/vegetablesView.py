class VegetablesView:
    # private variables
    __ALL_VEGETABLES = "1"
    __ONE_VEGETABLE = "2"
    __ADD_VEGETABLE = "3"
    __UPDATE_VEGETABLE = "4"
    __DELETE_VEGETABLE = "5"
    __EXTRACT_RECORDS = "6"
    __EXIT = "X"

    @staticmethod
    def display_menu():
        """
        Prints out on the console a menu of options for managing vegetables dataset
        :return:
        None
        """
        print(
            "\t\tOptions Menu\n\n"
            + "\t(1) View all vegetables\n"
            + "\t(2) View one vegetable\n"
            + "\t(3) Add vegetable\n"
            + "\t(4) Update vegetable\n"
            + "\t(5) delete vegetable\n"
            + "\t(6) Extract records to a file\n"
            + "\t(X) Exit\n"
        )

    @staticmethod
    def get_option_input():
        return input('Choose option: ')

    @staticmethod
    def list_all_veg(vegetables):
        """
        prints out on the console a list of the first 100 records in the dataset,
        and prints student name every 10 records
        :return:
        None
        """
        pass
        # TODO: print the passed list in a table (like in project 1).

    @staticmethod
    def display_one_veg():
        """
        Asks user for record id then prints out the details of that record.
        :return:
        None
        """
        pass
        # TODO: Get user input for the record id, get the record form a controller method then print it.

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
