"""New Window file."""
from libs.window import Window
from libs.button import Button, BigButton, MenuButton
from libs.table import Table


def new():
    """New Window function."""
    a = MenuButton().render()
    print(a)
    header_button = (
        (a, 'right'),
        # (Button(icon='properties').render(), 'right'),
    )
    new_win = Window("new_project",
                     "New Project",
                     (400, 280),
                     True,
                     *header_button)

    buttons = (
        (BigButton(name="dynamic_memory",
                   title="Dynamic Memory",
                   description="Some description about it."
                   ).render(), ),
        (BigButton(name="static_memory",
                   title="Static Memory",
                   description="Some description about it."
                   ).render(), ),
        (BigButton(name="pointer_memory",
                   title="Pointer Memory",
                   description="Some description about it."
                   ).render(), ),
    )

    table = Table(*buttons).render()
    new_win.add_item(table)
    new_win.render()
