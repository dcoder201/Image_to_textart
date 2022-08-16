# ascii_magic module convert image to colorful and greyscale text art
import ascii_magic

# getting image path and setting width and column ratio
my_art = ascii_magic.from_image_file(
    'johnwick.jpg',
    columns=200,
    width_ratio=2,
    ## if text art to be displayed on terminal
    # mode=ascii_magic.Modes.HTML_TERMINAL
)

## saving output as html file
# ascii_magic.to_html_file('ascii_art.html', my_art)

## displaying output to terminal
ascii_magic.to_terminal(my_art)
