"""
CP1404/CP5632 Practical
Sort Files Program V2.0
"""

import os
import shutil


def main():
    """Sort Files Program V2.0."""
    os.chdir('FilesToSort')
    extension_to_category = {}
    for filename in os.listdir('.'):
        # find files that don't start with "."
        if not filename[0] == ".":
            extension = filename.split(".")[-1]
            if extension not in extension_to_category:
                category = input("What category would you like to sort {} files into? "
                                 .format(extension))
                try:
                    os.mkdir(category)
                except FileExistsError:
                    pass
                extension_to_category[extension] = category
                shutil.move(filename, category + '/' + filename)
            else:
                category = extension_to_category[extension]
                shutil.move(filename, category + '/' + filename)


main()
