from view.vegetablesView import VegetablesView as View


def main():
    View.display_menu()
    selection = View.get_option_input()
    print("Loading...")


if __name__ == '__main__':
    main()
