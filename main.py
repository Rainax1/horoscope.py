"""
This script provides a command-line interface (CLI) and a graphical user interface (GUI) for fetching and displaying daily horoscope information. The application allows users to specify their zodiac sign, the desired day for the horoscope, and whether to display the output in color.

Dependencies:
- argparse: Used for parsing command-line arguments.
- src.api: Module containing the fetch_data function for fetching horoscope data.
- src.gui: Module containing the HoroscopeGUI class for the graphical user interface.

Usage:
1. To run the GUI, execute script without any arguments.
2. For CLI usage, execute the script with the following optional arguments:
   - -s/--sign: Zodiac sign (e.g., "Leo").
   - -d/--day: Day for which the horoscope is requested ("yesterday", "today", or "tomorrow").
   - -c/--color: If present, displays the output in color.

Example:
    # Run GUI
    python main.py

    # Fetch horoscope for Leo today in color
    python main.py -s Leo -d today -c

    # Fetch horoscope for Virgo tomorrow
    python main.py -s Virgo -d tomorrow
"""



import argparse
from src.api import fetch_data
from src.gui import HoroscopeGUI



def run_gui():
    root = HoroscopeGUI()
    root.mainloop()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--sign", type=str, help="this option takes your Zodiac Sign as an argument")
    parser.add_argument("-d", "--day", type=str, help="this option takes Day as and argument. You can choose between (Yesterday, Today, Tomorrow)")
    parser.add_argument("-c", "--color", default=False, action='store_true', help="colored  output")

    args = parser.parse_args()

    if (args.sign or args.day) and args.color:
        if (args.day != None):
            fetch_data(args.sign, args.day, color=True)
        else:
            fetch_data(args.sign, color=True)
    elif args.sign or args.day:
        if (args.day != None):
            fetch_data(args.sign, args.day)
        else:
            fetch_data(args.sign)
    else:
        run_gui()


if __name__ == "__main__":
    main()
