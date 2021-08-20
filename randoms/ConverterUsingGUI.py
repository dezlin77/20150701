from tkinter import *

def miles_to_km():
  miles = float(miles_input.get())
  km = miles * 1.609
  kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=2, row=0)

kilometer_result_label = Label(text="0")
kilometer_label = Label(text="km")
calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=2)


