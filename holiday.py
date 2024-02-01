"""Calculates the total price of the users holiday depending on a series of inputs."""
from simple_term_menu import TerminalMenu
from unit_functions import print_line, bold_text

def get_city_flight() -> str:
    """Asks user to choose which city to fly to from a list."""
    print(bold_text("\nwhich city would you like to fly to?"))
    cities = ["Agra", "Chicago", "Lisbon", "Nairobi", "Seoul"]
    terminal_menu = TerminalMenu(cities)
    menu_entry_index = terminal_menu.show()
    return cities[menu_entry_index]

def main() -> None:
    """Where all of the logic for the app is run."""
    print_line(char="=")
    print(f"{'*'*30}{bold_text('holiday.py')}{'*'*30}")
    print_line(char="=")

    city = get_city_flight()
    print(f"You chose to fly to {city}!")

    print_line(char="=")
    print(f"{'*'*27}{bold_text('holiday.py END')}{'*'*28}")
    print_line(char="=")

if __name__ == "__main__":
    main()