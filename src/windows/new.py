"""New Window file."""
from libs.window import Window
from libs.button import Button, BigButton
from libs.table import Table


def new():
    """New Window function."""
    header_button = (
        (Button(icon='properties').render(), 'right'),
    )
    new_win = Window("New Project", (400, 280), True, *header_button)

    buttons = (
        (BigButton(title="Sample Content",
                   description="Some description about it.",
                   icon="properties").render(), ),
        (BigButton(title="Static Memory",
                   description="Some description about it.",
                   icon="cancel").render(), ),
        (BigButton(title="Static Memory",
                   description="Some description about it.",
                   icon="add").render(), ),
    )

    table = Table(*buttons).render()
    new_win.add_item(table)
    new_win.render()
