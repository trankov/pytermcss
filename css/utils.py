# Small solution for random issues

import os
import sys

def cursor_reset():
    '''Soft reset without clearing screen'''

    sys.stdout.write('\x1b[!p')
    sys.stdout.flush()


def window_dimensions():
    '''Returns the dimensions of the window as a {'width' : int, 'height' : int}'''

    width, height = None, None

    try:
        width, height = os.get_terminal_size(sys.stdin.fileno())
    except (AttributeError, ValueError, OSError):
        try:
            width, height = os.get_terminal_size(sys.stdout.fileno())
        except (AttributeError, ValueError, OSError):
            width, height = 80, 25

    width = int(width) if width else 80
    height = int(height) if height else 25

    return {'width': width, 'height' : height}



if __name__ == '__main__':

# Test windows_dimensions()
    window_dimensions_test = window_dimensions()
    assert window_dimensions_test
    assert type(window_dimensions_test) is dict
    assert len(window_dimensions_test) == 2
    assert 'width', 'height' in window_dimensions_test
    assert type(window_dimensions_test['width']) is int
    assert type(window_dimensions_test['height']) is int
    assert window_dimensions_test['width'] and window_dimensions_test['width'] > 0
    assert window_dimensions_test['height'] and window_dimensions_test['height'] > 0
