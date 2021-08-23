class Style(object):

    def __init__(self, string = ''):
        self._result_string = str(string)
        self._template = ''
        self._apply = None

    def __call__(self, string: str = ''):
        self._result_string = str(string)
        return self

    def clear(self):
        self._template = ''
        return self

    def _transform(self, transformation):
        '''Supplements the template with a new value'''
        self._template = '\033[{}m{}'.format(transformation, self._template)

    @property
    def text(self):
        '''Return the text which will be stylized'''
        return self._result_string

    @text.setter
    def text(self, value):
        self._result_string = str(value)
        return self

    def display(self, value=''):
        if value:
            return '{}{}\033[m'.format(self._template, value)
        return self

    @property
    def bold(self):
        self._transform('1')
        return self

    @property
    def faint(self):
        self._transform('2')
        return self

    @property
    def italic(self):
        self._transform('3')
        return self

    @property
    def underline(self):
        self._transform('4')
        return self

    @property
    def blink(self):
        self._transform('5')
        return self

    @property
    def fastblink(self):
        self._transform('6')
        return self

    @property
    def invert(self):
        self._transform('7')
        return self

    @property
    def conceal(self):
        self._transform('8')
        return self

    @property
    def strike(self):
        self._transform('9')
        return self


    def color(self, color_code=0):
        '''
        Add one color value to template.
          n = Style().color(Style.RED)

        '''
        self._transform(color_code)
        return self


    def colors(self, *args):
        '''
        Adding 16-bit color codes from `args` to template. You can send
        any number of parameters, but only two first of them will be taken.
          Style('green text on blue').color(Style.GREEN, Style.BG_BLUE)

        '''
        [self._transform(i) for i in args[:2] if args]
        return self


    def bg256(self, color_code=0):
        self._transform('48;5;{}'.format(color_code))
        return self

    def fg256(self, color_code=0):
        self._transform('38;5;{}'.format(color_code))
        return self

    def colors256(self, foreground=0, background=0):
        self._transform('38;5;{}'.format(foreground))
        self._transform('48;5;{}'.format(background))
        return self


    def bgrgb(self, r=0, g=0, b=0):
        self._transform('48;2;{};{};{}'.format(r, g, b))
        return self

    def fgrgb(self, r=0, g=0, b=0):
        self._transform('38;2;{};{};{}'.format(r, g, b))
        return self


    def rgbcolors(self, foreground=(0, 0, 0), background=(0, 0, 0)):

        if any((type(background) is not tuple,
                type(foreground) is not tuple)):
            return self

        if any((len(foreground) != 3,
                len(background) != 3)):
            return self

        self._transform('38;2;{};{};{}'.format(*foreground))
        self._transform('48;2;{};{};{}'.format(*background))
        return self


    def apply(self, func_call):
        if callable(func_call):
            self._apply = func_call
        return self


    def __str__(self):
        if self._apply:
            self._result_string = self._apply(self._result_string)
        return '{}{}\033[m'.format(self._template, self._result_string)

    def __repr__(self):
        return self.__str__()
