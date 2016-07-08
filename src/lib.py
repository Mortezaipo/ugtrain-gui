"""Extra library which required for application.
"""
import gtk


def prompt(window, message):
    """Show prompt and get yes/no result from user.

    :param window: window object from gtk.
    :param message: text string for dialog message.
    :return: user clicked response on 'yes' or 'no'.
    :rtype: Boolean
    """
    dialog = gtk.MessageDialog(window, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                               gtk.MESSAGE_QUESTION,gtk.BUTTONS_YES_NO, message)
    response = dialog.run()
    dialog.destroy()
    if response == gtk.RESPONSE_YES:
        return True
    else:
        return False
