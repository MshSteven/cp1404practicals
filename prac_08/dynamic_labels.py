from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (1, 1, 0, 1)  # RGBA for yellow


class DynamicLabelsApp(App):
    """Design an app to show dynamic labels."""
    status_text = StringProperty()

    def __init__(self, **msh):
        """Construct main app."""
        super().__init__(**msh)
        # basic data (model) example - dictionary of names: label number
        self.name_to_label = {"Tom": "1", "Jerry": "2", "Coco": "3"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.name_to_label:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)
            temp_label.color = NEW_COLOUR
            self.root.ids.main.add_widget(temp_label)

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.main.clear_widgets()


DynamicLabelsApp().run()
