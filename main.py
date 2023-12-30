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

    args = parser.parse_args()

    if args.sign or args.day:
        if (args.day != None):
            fetch_data(args.sign, args.day)
        else:
            fetch_data(args.sign)
    else:
        run_gui()


if __name__ == "__main__":
    main()
