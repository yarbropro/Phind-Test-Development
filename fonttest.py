import pyfiglet
from rich import print
with open('fonts.txt', "w+") as file:
    fonts = pyfiglet.FigletFont.getFonts()
    for font in fonts:
        title = pyfiglet.figlet_format('Hacknet', font=f"{font}")
        file.write(f"{font}")
        file.write(f"{title}")
        print(font)
        print(f'[red]{title}[/red]')

#big_money-nw
#dos_rebel