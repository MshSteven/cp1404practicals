from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    message = StringProperty()

    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Press button to see the convert result"
        return self.root

    def handle_convert(self):
        """Handle calculation (could be button press or other call), output result to label widget."""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)

    def get_valid_miles(self):
        """Get text input from text entry widget, convert to float."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
