"""
CP1404 Prac_07 - GUI program to convert miles to kilometres
Cameron Attard
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609344


class ConvertMilesToKMProgram(App):

    km = StringProperty()

    def build(self):
        self.title = "Convert Miles to KM Program"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_press(self):
        self.km = self.root.ids.miles_input.text


ConvertMilesToKMProgram().run()
