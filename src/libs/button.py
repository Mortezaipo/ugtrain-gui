"""Buttons Library.
It contains several types of buttons.
"""

try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, Gdk
except ImportError:
    show('error', 'Python GTK3.0 library not found.')
    sys.exit(1)


class Button:
    """Button class.

    Args:
        text: Button label.
        icon: Button icon.
        style: Button style object.
    """
    def __init__(self, text=None, icon=None, style=None):
        self.text = text
        self.icon = Gtk.Image(stock="gtk-{}".format(icon)) if icon else None
        self.style = style

        # Enable button image property without changing system settings
        if self.text and self.icon:
            self.settings = Gtk.Settings.get_default()
            self.settings.props.gtk_button_images = True

    def render(self):
        """Render final results.

        Returns:
            Gtk button object
        """
        self.button = Gtk.Button(label=self.text, image=self.icon)
        return self.button


class BigButton(Button):
    """Big Button class.

    Args:
        title: Button title.
        description: Button description.
        icon: Button icon.
    """
    def __init__(self, title, description, icon=None):
        self.title = title
        self.description = description
        self.icon = Gtk.Image(stock="gtk-{}".format(icon)) if icon else None

    def render(self):
        """Render the final results.

        Returns:
            Gtk label object
        """
        self.button = Gtk.Label()
        self.button.set_name("big_button")
        self.button.set_justify(Gtk.Justification.LEFT)
        self.button.set_markup("<big><b>{}</b></big>\n<span>{}</span>"
                               .format(self.title, self.description))
        # self.button.set_state_flags(Gtk.StateFlags.INSENSITIVE, True)
        # self.button.set_line_wrap(True)
        return self.button
