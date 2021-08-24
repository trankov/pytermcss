import css
import textwrap

from functools import partial

blockquote = partial (textwrap.fill,
                      width=50, initial_indent=' >    ',
                      subsequent_indent = ' >  ', tabsize=4)

LF = css.LF

h1 = css.style().invert.bold.apply(str.upper)
h2 = css.style().invert.bold.apply(str.capitalize)
h3 = css.style().invert.apply(str.capitalize)

b = css.style().bold
i = css.style().italic
u = css.style().underline
bi = css.style().bold.italic
iu = css.style().underline.italic
biu = css.style().underline.bold.italic

li_dot = css.style().apply(lambda x: f'  \N{bullet} {x}')
li_bsq = css.style().apply(lambda x: f'  \N{black medium square} {x}')
li_wsq = css.style().apply(lambda x: f'  \N{white medium square} {x}')
li_trn = css.style().apply(lambda x: f'  \N{black right-pointing pointer} {x}')
li_hnd = css.style().apply(lambda x: f'  \N{white right pointing index} {x}')

quote = css.style().fgrgb(100, 200, 35).italic.apply(blockquote)

a = css.style().color(css.CYAN).underline



if __name__ == '__main__':

    print()
    print(h1('Let\'s evaluate the simplicity'), LF)

    print(h2('Text decoration'), LF)

    print(f'We here can print {b("bold")}, {i("italic")} and {u("underlined")} text.')
    print('As so as', bi('bold italic'), 'or', iu('underlined italic'), 'or', biu('all together.'), LF)

    print(h2('Unordered lists'), LF)

    print(h3('Dotted'), LF)
    [print(li_dot(animal)) for animal in ('Dog', 'Elephant', 'Rooster', 'Goat', 'Unicorn')]

    print(f"{LF}{h3('Squared (black)')}", LF)
    [print(li_bsq(fruit)) for fruit in ('Orange', 'Qiwi', 'Apple', 'Pear', 'Dragonfruit')]

    print(f"{LF}{h3('Squared (white)')}", LF)
    [print(li_wsq(veg)) for veg in ('Cucumber', 'Carrot', 'Cabbage', 'Potato', 'Zukini')]

    print(f"{LF}{h3('Triangled')}", LF)
    [print(li_trn(tree)) for tree in ('Palm', 'Oak', 'Pine', 'Elm', 'Yiggdrassile')]

    print(f"{LF}{h3('Handed')}", LF)
    [print(li_hnd(wear)) for wear in ('Hat', 'Suite', 'Panties', 'Boots', 'Wings')]

    print()
    print(h2('Blockquotes'), LF)
    print('Dear friend, yesterday you wrote to me:', LF)
    print(quote('I am not capable of close friendship: of two close friends, one is always the slave of the other, although frequently neither of them will admit it. I cannot be a slave, and to command in such circumstances is a tiresome business, because one must deceive at the same time.'), LF)
    print('I am strongly disagree with you, my heart.', LF)

    print(h2('Hyperlink-like'), LF)
    print(a('https://en.wikipedia.org/wiki/Hyperlink'), LF)
