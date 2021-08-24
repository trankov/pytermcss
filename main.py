import css

class CSS():
    h1 = css.style().\
         colors(css.YELLOW, css.BG_BLUE).\
         bold.\
         apply(lambda x: x.center(50).upper())

    ul_li = css.style().apply(lambda x: f'  \N{BULLET} {x}')

    ol_li = css.style().apply(lambda x: '  {{:>02}} {}'.format(x))

    b = css.style().bold
    i = css.style().italic
    bi = css.style().bold.italic


# print(CSS.h1('Program start...'))


# print('', 'Unsorted list:', '-'*14, '', sep='\n')

# for i in range(5):
#     print(CSS.ul_li(f'List item number {i+1}'))


# print('', 'Ordered list:', '-'*13, '', sep='\n')

# for num, fruit in enumerate(('Apples', 'Peaches', 'Melons', 'Plums')):
#     print(
#         str(
#             CSS.ol_li(fruit)
#         ).format(num + 1)
#     )

# print(CSS.b('The bold string'))
# print(CSS.b)
# CSS.b.text = 'The strong string'
# print(CSS.b)

# print(CSS.b.display('Am I looking strong?'))
# print(CSS.b) # Prints "This text is strong." again

# print(CSS.b('This text is still strong.'))
# print(CSS.b) # The value has been changed after call.

x = css.style('example')
print(f'{x}, {x.bold}')
print('{}, {}'.format(x, x.italic))
