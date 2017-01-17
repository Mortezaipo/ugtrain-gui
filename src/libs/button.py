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
    def __init__(self, name, title, description, icon=None, width=400):
        self.name = name
        self.title = title
        self.description = description
        self.icon = Gtk.Image(stock="gtk-{}".format(icon)) if icon else None
        self.width = width
        self.hbox_cols = 2 if self.icon else 1

    def render(self):
        """Render the final results.

        Returns:
            Gtk button object
        """
        self.hbox = Gtk.HBox(self.hbox_cols)
        self.hbox.set_homogeneous(False)

        self.label = Gtk.Label()
        self.label.set_justify(Gtk.Justification.LEFT)
        self.label.set_alignment(Gtk.Align.FILL, 0)
        self.label.set_markup("<big><b>{}</b></big>\n<span>{}</span>"
                              .format(self.title, self.description))

        self.hbox.pack_start(self.label, True, True, 0)
        if self.icon:
            self.hbox.pack_start(self.icon, False, False, 0)
        else:
            self.hbox.pack_start(
                Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE),
                False, False, 0)
        self.button = Gtk.Button()
        self.button.set_property("width-request", self.width)
        self.button.set_name(self.name)
        self.button.add(self.hbox)

        return self.button


class MenuButton:
    """Menu Button class."""

    def __init__(self):
        pass

    def render(self):
        parent_menu = Gtk.MenuBar()

        main_menu = Gtk.Menu()
        main_menu_item = Gtk.MenuItem("F")
        main_menu_item.set_submenu(main_menu)

        e = Gtk.MenuItem("Exit")
        main_menu.append(e)

        parent_menu.append(main_menu_item)
        return parent_menu
