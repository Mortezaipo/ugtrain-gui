"""New Window file."""
from libs.window import Window
from libs.button import Button, BigButton
from libs.table import Table


def new():
    """New Window function."""
    header_button = (
        (Button(icon='properties').render(), 'right'),
    )
    new_win = Window("New Project", (255, 280), True, *header_button)

    buttons = (
        (BigButton(title="Static Memory",
                   description="Some description about it.").render(), ),
        (BigButton(title="Static Memory",
                   description="Some description about it.").render(), ),
        (BigButton(title="Static Memory",
                   description="Some description about it.").render(), ),
    )

    table = Table(*buttons).render()
    new_win.add_item(table)
    new_win.render()
