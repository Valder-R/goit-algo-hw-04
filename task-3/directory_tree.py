from pathlib import Path
import sys
from colorama import Fore, Back, Style


def main():
    directory = Path(sys.argv[1])
    print(Fore.BLACK + Back.WHITE + directory.name + ":" + Style.RESET_ALL)
    
    try:
        for path in directory.iterdir():
            if path.is_dir():
                print(Fore.RED + "[DIR] " + path.name + Style.RESET_ALL)
            if path.is_file():
                print(Fore.GREEN + "[FILE] " + path.name + Style.RESET_ALL)
    
    except Exception as e:
        print(f"{e} - exception occured")

if __name__ == "__main__":
    main()