import customtkinter as ctk
from PIL import Image



class HoroscopeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Horoscope GUI")
        self.geometry("800x600")
        BG = ctk.CTkImage(light_image=Image.open("/home/raina/raina/projects/horoscope.py/src/icons/bg.jpg"),
                       dark_image=Image.open("/home/raina/raina/projects/horoscope.py/src/icons/bg.jpg"),
                          size=(800, 600))


        self.background_label = ctk.CTkLabel(self.master, image=BG,text="")
        self.background_label.place(relwidth=1, relheight=1)

        zodiac_images = {
                "Aries": "/home/raina/raina/projects/horoscope.py/src/icons/aries.jpg",
                "Taurus": "/home/raina/raina/projects/horoscope.py/src/icons/taurus.jpg",
                "Gemini": "/home/raina/raina/projects/horoscope.py/src/icons/gemini.jpg",
                "Cancer": "/home/raina/raina/projects/horoscope.py/src/icons/cancer.jpg",
                "Leo": "/home/raina/raina/projects/horoscope.py/src/icons/leo.jpg",
                "Virgo": "/home/raina/raina/projects/horoscope.py/src/icons/virgo.jpg",
                "Libra": "/home/raina/raina/projects/horoscope.py/src/icons/libra.jpg",
                "Scorpio": "/home/raina/raina/projects/horoscope.py/src/icons/scorpio.jpg",
                "Sagittarius": "/home/raina/raina/projects/horoscope.py/src/icons/sagittarius.jpg",
                "Capricorn": "/home/raina/raina/projects/horoscope.py/src/icons/capricorn.jpg",
                "Aquarius": "/home/raina/raina/projects/horoscope.py/src/icons/aquarius.jpg",
                "Pisces": "/home/raina/raina/projects/horoscope.py/src/icons/pisces.jpg",
                }
        
        # global zodiac_sign
        # for i in zodiac_images.keys():
        #     zodiac_sign = i 
        # # Create buttons for each zodiac sign
        # self.buttons = {}
        # for zodiac_sign, image_path in zodiac_images.items():
        #     self.buttons[zodiac_sign] = self.create_zodiac_button(image_path)

    # def create_zodiac_button(self, image_path):
        # # Create a button with the specified image
        # button_image = ctk.CTkImage(
        #                             light_image=Image.open(image_path),
        #                             dark_image=Image.open(image_path))

        # button = ctk.CTkButton(self.master,text=zodiac_sign, image=button_image, compound=ctk.BOTTOM)
        # button.pack(pady=10)  # Adjust padding as needed
        # return  button
    
        self.configure(highlightthickness=0, bd=0)

        self.create_buttons(zodiac_images)

    def create_buttons(self, zodiac_images):
        # Create a grid layout for the buttons
        row_num = 0
        col_num = 0
        for zodiac_sign, image_path in zodiac_images.items():
            button = self.create_zodiac_button(zodiac_sign, image_path)
            button.grid(row=row_num, column=col_num, padx=10, pady=10, sticky="nsew")

            col_num += 1
            if col_num == 3:
                col_num = 0
                row_num += 1

    def create_zodiac_button(self, zodiac_sign, image_path):

        button_width = int(800 / 3.5)
        button_height = int((600 - 100) / 4)

        # Create a button with the specified image and text
        button_image = ctk.CTkImage(
                                     light_image=Image.open(image_path),
                                     dark_image=Image.open(image_path))

        button = ctk.CTkButton(self, image=button_image, text=zodiac_sign, compound=ctk.BOTTOM, width=button_width, height=button_height)
        button.configure(image=button_image)
        return button





# ctk.set_appearance_mode("dark")
# app = HoroscopeGUI()
# app.mainloop()
