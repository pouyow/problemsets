import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    sfont = random.choice(fonts)
    figlet.setFont(font=sfont)
    it = input("Please put your text here: ")
    print(figlet.renderText(it))
elif len(sys.argv) > 1:
    if sys.argv[1] in ("-f", "--font"):
        z = sys.argv[2]
        if z in fonts:
            figlet.setFont(font=z)
            it = input("Please put your text here: ")
            print(figlet.renderText(it))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

