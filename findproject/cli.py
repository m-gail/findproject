from sys import argv
from projects import print_projects
from activate.list import print_activate_scripts


def main():
    if len(argv) < 2:
        print("Missing argument")
        return

    if argv[1] == "list":
        print_projects()
    elif argv[1] == "activate":
        print_activate_scripts(argv[2])
