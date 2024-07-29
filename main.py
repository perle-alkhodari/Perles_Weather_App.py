from Weather import Weather
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import ttkbootstrap as tb
from tkinter import END

# Initiation of the weather api.
# The weather api is from https://www.weatherapi.com/
data = Weather().location("Paris")


# Main app function.
def get_weather():
    global data, cloud, cloud_sun, dark, sun, thunder

    try:
        if len(user_entry.get()) != 0:
            data = Weather().location(user_entry.get())
            temperature = data["temp_c"]
            temp_c.config(text=str(temperature) + "°C", font=("Futura", 45, "bold"))
            region.config(text=data["name"] + ", " + data["country"])
            user_entry.delete(0, END)

            # Weather condition & picture swaps
            condition = data["condition"]
            if condition == "Partly cloudy" or condition == "Clear":
                image_label.config(image=cloud_sun)
            elif condition == "Overcast":
                image_label.config(image=dark)
            elif condition == "Sunny":
                image_label.config(image=sun)


    except KeyError:
        temp_c.config(
            font=("Futura", 20),
            text="Area Not Found")
        region.config(text="")


# Takes a file path and returns
# a photo object that can be given
# to the image= argument in the label
# constructors
def make_photo(file_path):
    cloud_sun_file_path = Image.open(file_path)
    resize = cloud_sun_file_path.resize(size=(80, 80))
    img = ImageTk.PhotoImage(resize)
    return img


def center_window(w, h, win):
    x_coor = int((win.winfo_screenwidth() / 2) - (w/2))
    y_coor = int((win.winfo_screenheight() / 2) - (h/2))
    win.geometry(f"{w}x{h}+{x_coor}+{y_coor}")


# Window
window = tb.Window(themename="solar", resizable=(False, False))
center_window(490, 250, window)
window.title("Perle's Weather App")

# My drawings
cloud = make_photo("Images/cloud.png")
cloud_sun = make_photo("Images/cloud_sun.png")
dark = make_photo("Images/dark.png")
rain = make_photo("Images/rain.png")
sun = make_photo("Images/sun.png")
thunder = make_photo("Images/thunder.png")

# Font for button
my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Futura", 15))

# Title Label
title = tb.Label(
    text="What's The Weather In...",
    font=("Futura", 20, "bold")
)
title.grid(row=0, column=0, padx=10, pady=(20, 10), columnspan=3)

# Region Entry
user_entry = tb.Entry(
    font=("Futura", 15),
    width=30
)
user_entry.grid(row=1, column=0, padx=(30, 10), columnspan=2)

# Submit button
submit = tb.Button(
    text="Done",
    width=4,
    style="success.Outline.TButton",
    command=get_weather
)
submit.grid(row=1, column=2)

# Drawing display
image_label = tk.Label(
    image=cloud
)
image_label.grid(row=2, column=0, padx=(20, 0), pady=(30, 0))

# Frame to hold temp and region labels
data_frame = tb.Frame(
    window,
)
data_frame.grid(row=2, column=1, sticky="ew", columnspan=2, pady=(20, 0))

# Temp
temp_c = tb.Label(
    data_frame,
    font=("Futura", 45, "bold"),
    text=str(data["temp_c"]) + "°C",
    justify="left",
)
temp_c.grid(row=0, column=0, sticky="s")

# Region
region = tb.Label(
    data_frame,
    font=("Futura", 13),
    text=data["name"] + ", " + data["country"],
    justify="left"
)
region.grid(row=1, column=0, sticky="n")

# End
window.mainloop()
