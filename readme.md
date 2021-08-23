# Python CSS-alike output library

## Introduction
There are already many excellent libraries that implement the output of colored text in the terminal window. The beauty of the situation is that they all offer us different approaches. Everyone of us can choose to their liking.

And, this library, which is currently under development, provides just one more approach. Which is seems most convenient to its author.

## Essence of the approach

The principle of W3C CSS is simple. We describe a display pattern and give it a name. Then we mark with that name different parts of the text.

In CSS, on the other hand, we can mark up the text directly in the line without creating a named template. This is so-called «inline styles».git

Python has many powerful tools for string formatting. On the other hand, visual formatting are not part of the standard library.

Most of third-party libraries are designed to simplify operations with escape codes. In this project, the standard Python features and implicit terminal capabilities are combined as a single solution. We declare styles using both.

Of course, this is not a literal implementation of CSS. It is not possible and it is not necessary. The goal of this project is that we can easily create patterns, easily implement them into printable strings, and they are easy to read in code.

Easy to write, easy to read and easy to understand.

## Installation

To be written.

## Ways to use

### Chain of transformations

The styles is organized through chain notation. It's easy to insert them directly into the lines you print.

```python
import css

print('This is the',
      css.style('strong').bold,
      'text example'.)

print('And this is the',
      css.style('strong oblique').bold.italic,
      'text example.')
```

You are responsible for the way your chain of transformation is organized. Conflicting instructions will lead to unpredictable results.

### Using strings with predefined styles

To apply the same design style to different strings, create an object of class `css.style` with the desired set of parameters.

```python
import css

b = css.style().bold
i = css.style().italic
bi = css.style().bold.italic
```

The objects you created are callable. They take a string as a single parameter and apply the specified style to it.

```python
print(b('This text is bold.'))
print(i('And this one is italic.'))
print(bi('This text is bold and italic.'))
```

Note that the string you called with the object will be stored in `text` property until you assign a new value to it. If you want just print a random string usng the style but keeping the main text value unchanged, use `display()` method.

```python
print(b('This text is bold.'))
print(b) # The same result as above

# Change stored text without calling:
b.text = 'This text is strong.'
print(b) # This text is strong.

# Print random text just using the style
print(b.display('Am I looking strong?'))
print(b) # Prints "This text is strong." again

print(b('This text is still strong.'))
print(b) # The value has been changed after call.
```

This behavior is a bit of a Zen violation _(There should be one-- and preferably only one --obvious way to do it)_. You can change `text` property both by calling and by assigning. Alternatively, you can simply apply the style to a random string without changing the value of `text`.

Different approaches can be useful depending on the use. Only the same method cannot be equally suitable for fast scripting, prototyping or complex projects. Just keep to some unified way when you design your application.

### Applying styles to predefined strings

Sometimes you need the same style for different strings. But sometimes you need to print the same text in different styles. You can reassign the style template as so as you reassign the text.

Before you can assign a new style at the object, you must clear the previous one. To do this, include the `clear()` method in your chain.

```python
>>> text = css.style(' some text ')
' some text '
>>> text.rgbcolors((200,200,0), (0, 33, 128))
# colored text output
>>>
>>>
>>> # You can clear the template and assign
>>> # a new one here on the same line
>>>
>>> text.clear().bg256(200)
# output of recolored text
>>> text.bold
# The modification will be applied to the existing
# ones because `clear()` method was ignored.
>>>
>>>
>>> # Also you can split the chain of transformations
>>> # into several lines for better readability
>>>
>>> text.clear()
' some text '
>>> text.colors(css.YELLOW, css.BG_RED).strike
# colored text with strikethrough
```

### Using Python functions

Yes, you can use functions in your styles declarations. It can be both built-in and your own.

To assing a function use the `apply` method.

```python
import css


# Let's begin to organize our style definitions

class CSS():
    h1 = css.style().\
         colors(css.YELLOW, css.BG_BLUE).\
         bold.\
         apply(lambda x: x.center(50).upper())

    h2 = css.style().bold.apply(str.title)


print(CSS.h1('Program start...'))

# Prints bold yellow text at center of blue
# rectangle in uppercase

print(CSS.h2('this is headline'))

# Prints 'This Is Headline' with bold type

```

The `apply` method can be declared only once. If you combine several `apply` methods in one chain, only the last one will be executed. If you want to apply more than one function, use `lambda` or define your own.

One of the useful features is the built-in Python string formatting.

```python
import css


class CSS():
    ul_li = css.style().apply(lambda x: f'  \N{BULLET} {x}')


print('', 'Unsorted list:', '-'*14, '', sep='\n')

for i in range(5):
    print(CSS.ul_li(f'List item number {i+1}'))


#
# Unsorted list:
# --------------
#
#   • List item number 1
#   • List item number 2
#   • List item number 3
#   • List item number 4
#   • List item number 5
```

When using templates, remember that you're not working with `str` objects, but with objects of the `css.style` class. This means that if you want to use nested formatting, you'll have to explicitly convert it to a string. The methods of the `str` class do not work with the string representation of objects returned by the `__str__` method. This applies in its entirety to the `str.format` method.

```python
import css


class CSS():
    ol_li = css.style().apply(lambda x: '  {{:>02}} {}'.format(x))

    # Will be '  {:>02} text' after applying style,
    # so we can use str.format() with it


print('', 'Ordered list:', '-'*13, '', sep='\n')

for num, fruit in enumerate(('Apples', 'Peaches', 'Melons', 'Plums')):
    print(
        str(
            CSS.ol_li(fruit)
        ).format(num + 1)
    )

#
# Ordered list:
# -------------
#
#   01 Apples
#   02 Peaches
#   03 Melons
#   04 Plums

```

### Using colors

There are three different ways to use colors in POSIX terminals. First, 16 colors palette. Second, 256 colors palette. Third, full RGB color palette.

Colors could be applied to foreground and to background of string. Both colors may belong to different palettes.

This library supports all palettes, with two methods for 16-color and three methods for 256 and RGB. Two methods are for foreground and background. They takes only one parameter. And third method takes foreground and background parameters in the same palette.

#### 16-colors palette:
 - `color(color_code: int)`
 - `colors(*args)`

Actually, you can use only `colors` method, as it itakes any number of arguments, but using only first and second (if passed). Foreground and background values for 16-colors palette are different, so you can pass it in any оrder.

Colors predefined constants keeping in `css` class, so you can invoke them as arguments.

```python
>>> style.css('red text').color(css.RED)
>>> style.css('green background').color(css.BG_GREEN)
>>> style.css('red text at green background').colors(css.RED, css.BG_GREEN)
>>> style.css('red text at green background').color(css.RED).color(css.BG_GREEN)
```

#### 256 colors palette:
 - `bg256(color_code: int)`
 - `fg256(color_code: int)`
 - `colors256(foreground: int, background: int)`

 You can look at the color definitions [in Wikipedia](https://en.wikipedia.org/w/index.php?title=ANSI_escape_code&section=15#8-bit).

 ```python
 >>> style.css('red text').fg256(196)
 >>> style.css('green background').bg256(70)
 >>> style.css('red text at green background').colors256(196, 70)
 ```

#### True Color (RGB) palette:

 - `bgrgb(r: int, g: int, b: int)`
 - `fgrgb(r: int, g: int, b: int)`
 - `rgbcolors(foreground: tuple, background: tuple)`

Usage examples:

```python
 >>> style.css('red text').fgrgb(255, 0, 0)
 >>> style.css('green background').bgrgb(0, 255, 0)
 >>> style.css('red text at green background').rgbcolors((255, 0, 0), (0, 255, 0))
 ```

### Typefaces

Typefaces are the simplest members of the style chain. They don't have arguments and are separated by a dot in any order.

The standard typefaces are as follows:
`bold`, `faint`, `italic`, `underline`, `blink`, `fastblink`, `invert`, `conceal`, `strike`.

Not all terminals fully support these parameters.

```python
>>> css.style('Example').bold
>>> css.style('Example').italic
>>> css.style('Example').invert.strike
>>> css.style('Example').color(css.RED).underline.apply(str.lower)
```

## Nota Bene

Different terminal programs and operating systems support different features and require different implementations. This problem has not been solved at the moment. The current implementation is only being developed for POSIX.
