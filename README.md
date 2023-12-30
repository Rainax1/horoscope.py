
> [!WARNING]
> This software is unfinished.

# TODO
- [ ] Add json caching

# Horoscope.py
A simple Python application that provides daily horoscope information for different zodiac signs. This project consists of three main components: `api.py` for fetching horoscope data from an API, `gui.py` for a graphical user interface, and `main.py` to run the application from the command line.

# Features
Horoscope Fetching: `api.py` fetches horoscope data from The [Astrologer](http://sandipbgt.com/theastrologer/api/) API using the specified zodiac sign and day (default is today).

Graphical User Interface (GUI): `gui.py` offers a user-friendly interface to select and view horoscopes for different zodiac signs.

Command-Line Interface (CLI): `main.py` allows users to run the application from the command line, providing options to specify the zodiac sign and day.

> If no arguments are provided to `main.py`, the default behavior is to launch the graphical user interface (GUI). Alternatively, if arguments are specified, the application will generate results in the command-line interface (CLI).



# Getting Started

Clone the repository:

```bash
git clone https://github.com/Rainax1/horoscope.py.git
cd horoscope.py
```

# Install dependencies:

```bash
pip install -r requirements.txt
```

# Run the GUI:
```bash
python main.py
```

# To fetch a specific horoscope from the command line, use the following options:

```bash
python main.py -s <zodiac_sign> -d <day>
or
python main.py -h
```


# Project Structure

`main.py`: The main entry point for the application, allowing users to run the app from the command line or GUI.

`api.py`: Fetches horoscope data from the API and handles caching.

`gui.py`: Provides a graphical user interface using the customtkinter library for selecting zodiac signs and displaying horoscope.


# Dependencies

[customtkinter](https://github.com/TomSchimansky/CustomTkinter): A customized version of the Tkinter library for a more modern look.

[PIL](https://pillow.readthedocs.io/en/stable/): Python Imaging Library for working with images.

[requests](https://requests.readthedocs.io/en/latest/): HTTP library for making API requests.

[requests-cache](https://requests-cache.readthedocs.io/en/stable/): Caching library for storing API responses.

# License

This project is licensed under the MIT License.

