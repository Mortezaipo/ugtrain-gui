"""Rich print libraray."""

# Text colors list for terminal output
text_colors = {
    'normal': '\033[0m',
    'error': '\033[91m',
    'success': '\033[92m',
    'warning': '\033[93m',
    'info': '\033[94m',
}


def show(mode='normal', *args):
    """Main print function.

    Args:
        mode: output color type.
        *args: list of all data which to be printed.
    Returns:
        None
    """
    message = " ".join(map(str, args))
    print(text_colors.get(mode, 'normal'), message, text_colors.get('normal'))
