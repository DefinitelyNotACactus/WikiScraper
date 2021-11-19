from browser import EngineBrowserCLI

def main():
    cli = EngineBrowserCLI()
    cli.main_loop()

if __name__ == '__main__':
    from sys import argv
    if '-h' in argv or '--help' in argv:
        print('Usage: python Scrapper.py [--specials] [--full-links]')
    else: main()
