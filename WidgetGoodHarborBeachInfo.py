from tkinter import *
import requests
import re
from bs4 import BeautifulSoup


root = Tk()
root.title('Good Harbor Beach Information')
root.geometry('700x500')

class Title_widget(Frame):
	def __init__(self, parent, label_text):
		super().__init__(master = parent)
		self.columnconfigure(0, weight=1)
		Label(self, text=label_text, font=("Helvetica", 22)).grid(row=0, column=0, sticky="n")
		self.pack(expand=True, fill="both", padx=10, pady=10)

class Label_widget(Frame):
	def __init__(self, parent, label_text1, label_text2, label_text3):
		super().__init__(master = parent)

		# Set up our grid stuff
		self.rowconfigure(0, weight=1)
		self.columnconfigure((0,2), weight=1, uniform='z')

		# Create our widgets
		Label(self, text=label_text1, font=("Helvetica", 18)).grid(row=0, column=0, sticky="nsew")
		Label(self, text=label_text2, font=("Helvetica", 18)).grid(row=0, column=1, sticky="nsew")
		Label(self, text=label_text3, font=("Helvetica", 18)).grid(row=0, column=2, sticky="nsew")


		self.pack(expand=True, fill="both", padx=10, pady=0)

			
class Info_widget(Frame):
	def __init__(self, parent, label_text1, label_text2, label_text3):
		super().__init__(master = parent)

		# Set up our grid stuff
		self.rowconfigure(0, weight=1)
		self.columnconfigure((0,2), weight=1, uniform='z')

		# Create our widgets
		Label(self, text=label_text1, font=("Helvetica", 14)).grid(row=0, column=0, sticky="nsew")
		Label(self, text=label_text2, font=("Helvetica", 14)).grid(row=0, column=1, sticky="nsew")
		Label(self, text=label_text3, font=("Helvetica", 14)).grid(row=0, column=2, sticky="nsew")


		self.pack(expand=True, fill="both", padx=10, pady=0)

class Label_widget_sun(Frame):
	def __init__(self, parent, label_text1, label_text2, label_text3):
		super().__init__(master = parent)

		# Set up our grid stuff
		self.rowconfigure(0, weight=1)
		self.columnconfigure((0,2), weight=1, uniform='z')

		# Create our widgets
		Label(self, text=label_text1, font=("Helvetica", 18)).grid(row=0, column=0, sticky="nsew")
		Label(self, text=label_text2, font=("Helvetica", 18)).grid(row=0, column=1, sticky="nsew")
		Label(self, text=label_text3, font=("Helvetica", 14)).grid(row=0, column=2, sticky="nsew")


		self.pack(expand=True, fill="both", padx=10, pady=0)

			
class Info_widget_sun(Frame):
	def __init__(self, parent, label_text1, label_text2, label_text3):
		super().__init__(master = parent)

		# Set up our grid stuff
		self.rowconfigure(0, weight=1)
		self.columnconfigure((0,2), weight=1, uniform='z')

		# Create our widgets
		Label(self, text=label_text1, font=("Helvetica", 14)).grid(row=0, column=0, sticky="nsew")
		Label(self, text=label_text2, font=("Helvetica", 14)).grid(row=0, column=1, sticky="nsew")
		Label(self, text=label_text3, font=("Helvetica", 18)).grid(row=0, column=2, sticky="nsew")


		self.pack(expand=True, fill="both", padx=10, pady=0)

class Button_widget(Frame):
    def __init__(self, parent, button_text):
        super().__init__(master = parent)

        # Set up our grid stuff
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='z')

        Button(self, text=button_text, command=lambda: self.change()).grid(row=0, column=0, sticky="n")
        self.pack(expand=True, fill="both", padx=10, pady=0)

    def change(self):
        print("Doubt you'll see this, but love ya mom!")
        root.mainloop()

class Spacing_widget(Frame):
    def __init__(self, parent, label_text1):
        super().__init__(master = parent)

        # Set up our grid stuff
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='z')

        # Create our widgets
        Label(self, text=label_text1, font=("Helvetica", 6)).grid(row=0, column=0, sticky="nsew")
        self.pack(expand=True, fill="both", padx=10, pady=0)

tideurl = "https://www.surf-forecast.com/breaks/Good-Harbor-Beach/tides/latest"
tempurl = "https://www.surf-forecast.com/breaks/Good-Harbor-Beach/seatemp"
tidesoup = BeautifulSoup(requests.get(tideurl).text, 'html.parser')
tempsoup = BeautifulSoup(requests.get(tempurl).text, 'html.parser')

high_tide_times = tidesoup.find_all("span", attrs={"class":"tide-time__time tide-time__time--high"}, limit=4)
tide_heights = tidesoup.find_all("span", attrs={"class":"tide-time__height"})
low_tide_times = tidesoup.find_all("span", attrs={"class":"tide-time__time tide-time__time--low"}, limit=4)
high_tide_heights = tide_heights[:4]
low_tide_heights = tide_heights[56:60]
date_day = (tidesoup.find("th", attrs={"class":"tide-table__day"})).text
sunrise = (tidesoup.find("td", attrs={"class":"tide-table__part tide-table__part--sun tide-table__part--first-shadow"})).text
sunset = (tidesoup.find("td", attrs={"class":"tide-table__part tide-table__part--sun tide-table__part--sunset tide-table__part--last-shadow"})).text
sun_next_day = (tidesoup.find("td", attrs={"class":"tide-table__part tide-table__part--sun tide-table__part--last"})).text
if sun_next_day[0] == ' ':
    sun_next_day = sun_next_day[1:]
sunrise_nd, sunset_nd = sun_next_day.split(' ', 1)

moonrise = ""
moonphase = ""
if (tidesoup.find("td", attrs={"class":"tide-table__part tide-table__part--moon tide-table__part--first-shadow"})):
    moonrise = (tidesoup.find("td", attrs={"class":"tide-table__part tide-table__part--moon tide-table__part--first-shadow"})).text
    match = re.search(r'\((.*?)\)', moonrise)
    moonphase = match.group(1)
    moonrise = moonrise[-7:]
    moonrise = moonrise.replace(" ", "")
moonset = ""
if (tidesoup.find("td", attrs={"class":"tide-table__part tide-table__part--moon tide-table__part--last-shadow"})):
    moonset = (tidesoup.find("td", attrs={"class":"tide-table__part tide-table__part--moon tide-table__part--last-shadow"})).text
    if (moonphase == ""):
        match = re.search(r'\((.*?)\)', moonset)
        moonphase = match.group(1)
		
    moonset = moonset[-7:]
    moonset = moonset.replace(" ", "")

water_temp_C = (tempsoup.find("span", attrs={"class":"sea-temp__forecast-text sea-temp__forecast-text--hero"})).text
match = re.search(r'\d+\.\d+', water_temp_C)
temp_num = float(match.group())
water_temp_F_float = round(((temp_num * 1.8) + 32), 1)
water_temp_F = str(water_temp_F_float) + " °F"


if moonrise == "":
	moonrise == " "
if moonset == "":
	moonset = " "
Title_widget(root, date_day)
Label_widget(root, "High Tide", "Low Tide", "Water Temperature")
Info_widget(root, str(high_tide_times[0].text) + " - " + str(high_tide_heights[0].text) + "m", str(low_tide_times[0].text) + " - " + str(low_tide_heights[0].text) + "m", water_temp_C)
Info_widget(root, str(high_tide_times[1].text) + " - " + str(high_tide_heights[1].text) + "m", str(low_tide_times[1].text) + " - " + str(low_tide_heights[1].text) + "m", water_temp_F)
Spacing_widget(root, " ")
Label_widget(root, "Sunrise", "Moon Rise", " ")
Info_widget_sun(root, sunrise, moonrise, "   Moon Phase")
Label_widget_sun(root, "Sunset", "Moon Set", moonphase)
Info_widget_sun(root, sunset, moonset, " ")
Title_widget(root, "Tomorrow")
Label_widget(root, "High Tide", "Low Tide", "Sunset/Sunrise")
Info_widget(root, str(high_tide_times[2].text) + " - " + str(high_tide_heights[2].text) + "m", str(low_tide_times[2].text) + " - " + str(low_tide_heights[2].text) + "m", sunrise_nd)
Info_widget(root, str(high_tide_times[3].text) + " - " + str(high_tide_heights[3].text) + "m", str(low_tide_times[3].text) + " - " + str(low_tide_heights[3].text) + "m", sunset_nd)
Spacing_widget(root, " ")
Button_widget(root, "Refresh")
Spacing_widget(root, " ")

root.mainloop()
