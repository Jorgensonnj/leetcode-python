#!/usr/bin/env python

import sys
import re
import importlib

def help():
    print("Invalid use. Example main.py <option>")
    print("Possible options:")
    print(" - 200_number_of_islands")


def get_dir(args):
    if len(args) == 1 or len(args) > 2:
        help()
        quit()
    else:
        return args[1]

def main():
    dir_option = get_dir(sys.argv)

    # Return a string in the '<package_name>.<module_name>'
    # format. Packages are directories and a module is a
    # specific file in that directory
    option = re.sub(r'\/$', "", dir_option) + ".main"

    module = importlib.import_module(option)
    module.main()

if __name__ == "__main__":
    main()
