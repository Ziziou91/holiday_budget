"""Unit and helper functions for holiday.py."""

def print_line(char="-", count=70) -> None:
    """Prints a line of characters for formatting in the terminal."""
    print(f"{char*count}")

def bold_text(text: str) -> str:
  """Returns a bolded string for printing."""
  return "\033[1m" + text + "\033[0m"