"""Unit and helper functions for holiday.py."""
import json

def print_line(char="-", count=70) -> None:
    """Prints a line of characters for formatting in the terminal."""
    print(f"{char*count}")

def bold_text(text: str) -> str:
  """Returns a bolded string for printing."""
  return "\033[1m" + text + "\033[0m"

def load_json(file_name: str) -> str:
    """Opens and loads a json file then returns."""
    try:
        file = open(file_name, "r", encoding="UTF-8")
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Error! {file_name} is an invalid path.") from exc  
    else:
        with file:
            data = json.load(file)
            return data
