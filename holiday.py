"""Calculates the total price of the users holiday depending on a series of inputs."""
from simple_term_menu import TerminalMenu
from unit_functions import print_line, bold_text, load_json

def get_city_flight(city_data: dict) -> str:
    """Asks user to choose which city to fly to from a list."""
    print(bold_text("\nwhich city would you like to fly to?"))
    cities = list(city_data.keys())
    terminal_menu = TerminalMenu(cities)
    menu_entry_index = terminal_menu.show()
    print(cities[menu_entry_index])
    return cities[menu_entry_index]

def get_hotel_stars() -> str:
    """Asks user to choose which city to fly to from a list."""
    stars = ["three_stars", "four_stars", "five_stars"]
    print(bold_text("\nWhat sort of hotel would you like to stay in?"))
    terminal_menu = TerminalMenu([i.replace("_", " ") for i in stars])
    menu_entry_index = terminal_menu.show()

    print(stars[menu_entry_index])

    return stars[menu_entry_index]

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

def hotel_cost(num_nights: int, hotel_stars: str, city: str, city_data: dict) -> int:
    """Gets the hotel price from city data, multiplies by the number of nights and then returns."""
    hotel_price = city_data[city]["hotels"][hotel_stars]
    return hotel_price * num_nights

def plane_cost(city: str, city_data: dict) -> int:
    """Returns the flight cost from city_data for the chosen city."""
    return city_data[city]["flight_cost"]

def car_rental(car_days: int) -> int:
    """Returns the total cost of car rental."""
    return car_days * 80

def holiday_cost(hotel_total: int, plane_total: int, car_total: int) -> int:
    """Totals up the cost of hotels, flights and car rental then returns."""
    return hotel_total + plane_total + car_total

def main() -> None:
    """Where all of the logic for the app is run."""
    print_line(char="=")
    print(f"{'*'*30}{bold_text('holiday.py')}{'*'*30}")
    print_line(char="=")

    city_data = load_json("cities.json")
    city = get_city_flight(city_data)
    hotel_stars = get_hotel_stars()

    print("How many nights will you be needing a hotel for?")
    num_nights = get_integer()
    print(f"{num_nights} nights")
    
    print("How many days will you be hiring a car for? If you don't need a car type 0")
    car_days = get_integer()
    
    hotel_total = hotel_cost(num_nights, hotel_stars, city, city_data)
    plane_total = plane_cost(city, city_data)
    car_total = car_rental(car_days)
    total_cost = holiday_cost(hotel_total, plane_total, car_total)
    
    print(f"The total cost of your holiday is £{total_cost}")
    print_line(char="=")
    print(f"{'*'*27}{bold_text('holiday.py END')}{'*'*28}")
    print_line(char="=")

if __name__ == "__main__":
    main()