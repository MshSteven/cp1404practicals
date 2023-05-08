from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Create an app to show boxlayout."""
    def build(self):
        """Construct app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        """Handle with the button greet"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle with the button clear"""
        self.root.ids.output_label.text = 'Enter your name'
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
