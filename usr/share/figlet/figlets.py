import pyfiglet
import sys
import random
# expects zero or two command line arguments
# zero if the user would like to output text in a random font
# two if the user would like to output text in a specfic font
# in which case the first of the tow should be -f or --font, and the second of the the two should be the name of the font
# prompts the user for a str of text
# outputs the text in the desired font

# f = pyfiglet.Figlet(font='slant')
# print(f.renderText('hello world'))


lst_of_fonts = [
    "3-d",
    "3x5",
    "5lineoblique",
    "acrobatic",
    "alligator",
    "alligator2",
    "alphabet",
    "avatar",
    "banner",
    "banner3-D",
    "banner3",
    "banner4",
    "barbwire",
    "basic",
    "bell",
    "big",
    "bigchief",
    "binary",
    "block",
    "bubble",
    "bulbhead",
    "calgphy2",
    "calligraphy",
    "catwalk",
    "chunky",
    "coinstak",
    "colossal",
    "computer",
    "contessa",
    "contrast",
    "cosmic",
    "cosmike",
    "cricket",
    "cyberlarge",
    "cybermedium",
    "cybersmall",
    "diamond",
    "digital",
    "dotmatrix",
    "doom",
    "drpepper",
    "eftichess",
    "eftifont",
    "eftipiti",
    "eftirobot",
    "eftitalic",
    "eftiwall",
    "eftiwater",
    "epic",
    "fender",
    "fourtops",
    "fuzzy",
    "goofy",
    "gothic",
    "graffiti",
    "hollywood",
    "invita",
    "isometric1",
    "isometric2",
    "isometric3",
    "isometric4",
    "italic",
    "ivrit",
    "jazmine",
    "jerusalem",
    "katakana",
    "kban",
    "larry3d",
    "lcd",
    "lean",
    "letters",
    "linux",
    "lockergnome",
    "madrid",
    "marquee",
    "maxfour",
    "mike",
    "mini",
    "mirror",
    "mnemonic",
    "morse",
    "moscow",
    "nancyj-fancy",
    "nancyj-underlined",
    "slant",
    "rectangles"
]


cla = sys.argv

if len(cla) == 3:
            if cla[1] == '-f' or cla[1] == '--font':
                if cla[2] in lst_of_fonts:
                    user_text = "HTML CSS BOILER PLATE CREATED"
                    # font = random.choice(pyfiglet.FigletFont.getFonts())
                    f = pyfiglet.Figlet(font=cla[2])
                    print(f.renderText(user_text))
                else:
                    sys.exit()
            else:
                sys.exit()
elif len(cla) == 1:
            user_text = "HTML CSS BOILER PLATE CREATED"
            font = random.choice(pyfiglet.FigletFont.getFonts())
            f = pyfiglet.Figlet(font=font)
            print(f.renderText(user_text))
else:
    sys.exit()




# c = sys.argv
# print(len(c))
# print('hello', cla1, cla2)
