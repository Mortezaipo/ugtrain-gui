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
    def __init__(self, title, description, icon, width=400):
        self.title = title
        self.description = description
        self.icon = Gtk.Image(stock="gtk-{}".format(icon)) if icon else None
        self.width = width

    def render(self):
        """Render the final results.

        Returns:
            Gtk button object
        """
        self.hbox = Gtk.HBox(2)
        self.hbox.set_homogeneous(False)

        self.label = Gtk.Label()
        self.label.set_justify(Gtk.Justification.LEFT)
        self.label.set_alignment(Gtk.Align.FILL, 0)
        self.label.set_markup("<big><b>{}</b></big>\n<span>{}</span>"
                              .format(self.title, self.description))

        self.hbox.pack_start(self.label, True, True, 0)
        self.hbox.pack_start(self.icon, False, False, 0)

        self.button = Gtk.Button()
        self.button.set_property("width-request", self.width)
        self.button.set_name("big_button")
        self.button.add(self.hbox)

        return self.button
