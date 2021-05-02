"""
CP1404 Prac_07 - GUI program to convert miles to kilometres
Cameron Attard
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.609344


class ConvertMilesToKMProgram(App):

    def build(self):
        self.title = "Convert Miles to KM Program"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_miles_to_km(self):
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM
        self.root.ids.km_output.text = str(km)

    def handle_increment(self, increment):
        new_miles = self.get_valid_miles() + increment
        self.root.ids.miles_input.text = str(new_miles)
        self.calculate_miles_to_km()

    def get_valid_miles(self):
        miles = float(self.root.ids.miles_input.text)
        return miles


ConvertMilesToKMProgram().run()
