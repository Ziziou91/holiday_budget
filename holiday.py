"""Calculates the total price of the users holiday depending on a series of inputs."""
from simple_term_menu import TerminalMenu
from unit_functions import print_line, bold_text, load_json

def get_city_flight() -> str:
    """Asks user to choose which city to fly to from a list."""
    print(bold_text("\nwhich city would you like to fly to?"))
    cities = ["Agra", "Chicago", "Lisbon", "Nairobi", "Seoul"]
    terminal_menu = TerminalMenu(cities)
    menu_entry_index = terminal_menu.show()
    return cities[menu_entry_index]

def get_integer() -> int:
    """Takes a user input, ensures it can be cast as an integer and then returns."""
    user_str = input("Type in your integer here: ")
    try:
        user_int = int(user_str)
    except ValueError:
        print(f"{'='*10}Error! {user_str} is not a valid integer. Please try again.{'='*10}")
        return get_integer()
    else:
        return user_int

def main() -> None:
    """Where all of the logic for the app is run."""
    print_line(char="=")
    print(f"{'*'*30}{bold_text('holiday.py')}{'*'*30}")
    print_line(char="=")
    city_data = load_json("cities.json")
    print(city_data)
    city_flight = get_city_flight()
    print(f"You chose to fly to {city_flight}!")
    print("How many nights will you be needing a hotel for?")
    num_nights = get_integer()
    print(f"Enjoy your stay of {num_nights} nights!")


    print_line(char="=")
    print(f"{'*'*27}{bold_text('holiday.py END')}{'*'*28}")
    print_line(char="=")

if __name__ == "__main__":
    main()