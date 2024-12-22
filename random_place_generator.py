import random
import tkinter as tk
from tkinter import ttk
from geopy.geocoders import Nominatim
import webbrowser

def generate_random_coordinates():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude

def create_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps/@{latitude},{longitude},10z"

def get_place_description(latitude, longitude):
    geolocator = Nominatim(user_agent="random_place_generator")
    try:
        location = geolocator.reverse((latitude, longitude), language="en")
        if location and location.address:
            return location.address
        else:
            return "Unknown location"
    except Exception as e:
        return "Error retrieving location"

def open_link(event):
    webbrowser.open_new(event.widget.cget("text"))

def on_button_click():
    latitude, longitude = generate_random_coordinates()
    google_maps_link = create_google_maps_link(latitude, longitude)
    place_description = get_place_description(latitude, longitude)
    result_label.config(text=f"Location: {place_description}")
    link_label.config(text=google_maps_link)

def main():
    global result_label, link_label

    root = tk.Tk()
    root.title("Random Place Generator")
    root.resizable(False, False)

    button = ttk.Button(root, text="Random Place In The World", command=on_button_click)
    button.pack(pady=20)

    result_label = tk.Label(root, text="", wraplength=400, justify="left")
    result_label.pack(pady=10)

    link_label = tk.Label(root, text="", fg="blue", cursor="hand2", wraplength=400, justify="left")
    link_label.pack(pady=10)
    link_label.bind("<Button-1>", open_link)

    root.geometry("500x300")
    root.mainloop()

if __name__ == "__main__":
    main()
