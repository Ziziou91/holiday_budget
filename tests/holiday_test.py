"""Tests for functions in holiday."""
from holiday import hotel_cost, plane_cost, car_rental, holiday_cost

cities = {
    "Agra" : {
        "flight_cost" : 650,
        "hotels" : {
            "three_stars" : 35,
            "four_stars" : 65,
            "five_stars" : 105
        }
    },
    "Chicago" : {
        "flight_cost" : 850,
        "hotels" : {
            "three_stars" : 40,
            "four_stars" : 85,
            "five_stars" : 160
        }
    },
}

# hotel_cost tests
def test_hotel_cost_returns_an_integer():
    """Ensures that hotel_cost returns an integer."""
    assert isinstance(hotel_cost(5, "three_stars", "Agra", cities), int)

def test_hotel_cost_returns_expected_value():
    """Ensures that hotel_cost returns the expected value."""
    assert hotel_cost(5, "three_stars", "Agra", cities) == 175
    assert hotel_cost(4, "four_stars", "Agra", cities) == 260
    assert hotel_cost(3, "five_stars", "Chicago", cities) == 480

# plane_cost tests
def test_plane_cost_returns_an_integer():
    """Ensures that plane_cost returns an integer."""
    assert isinstance(plane_cost("Agra", cities), int)

def test_plane_cost_returns_expected_value():
    """Ensures that plane_cost returns the expected value."""
    assert plane_cost("Agra", cities) == 650
    assert plane_cost("Chicago", cities) == 850

# car_rental tests
def test_car_rental_returns_an_integer():
    """Ensures that car_rental returns an integer."""
    assert isinstance(car_rental(5), int)

def test_car_rental_returns_expected_value():
    """Ensures that car_rental returns the expected value."""
    assert car_rental(5) == 400
    assert car_rental(2) == 160

# holiday_cost tests
def test_holiday_cost_returns_an_integer():
    """Ensures that car_rental returns an integer."""
    assert isinstance(holiday_cost(100, 200, 300), int)

def test_holiday_cost_returns_expected_value():
    """Ensures that holiday_cost returns the expected value."""
    assert holiday_cost(100, 200, 300) == 600
    assert holiday_cost(300, 400, 500) == 1200
