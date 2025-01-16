from pathlib import Path
import sys
from colorama import Fore, Back, Style


def directory_tree(directory :Path, deep:int):
    try:
        for path in directory.iterdir():
            if path.is_dir():
                print(Fore.RED + "-" * deep + ">" + "[DIR] " + path.name + Style.RESET_ALL)
                directory_tree(directory / path.name, deep+1 )
            if path.is_file():
                print(Fore.GREEN + "-" * deep + ">" + "[FILE] " + path.name + Style.RESET_ALL)
    
    except Exception as e:
        print(f"{e} - exception occured")


def main():
    directory = Path(sys.argv[1])
    print(Fore.BLACK + Back.WHITE + directory.name + ":" + Style.RESET_ALL)
    directory_tree(directory, 0)

if __name__ == "__main__":
    main()