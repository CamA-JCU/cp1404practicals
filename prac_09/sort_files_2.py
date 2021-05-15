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
            # print(extension)
            if extension not in extension_to_category:
                category = input("What category would you like to sort {} files into? ".format(extension))
                try:
                    os.mkdir(category)
                except FileExistsError:
                    pass
                extension_to_category[extension] = category
                shutil.move(filename, category + '/' + filename)
                # print("Move {} to {}".format(filename, category))
            else:
                category = extension_to_category[extension]
                # print("Move {} to {}".format(filename, category))
                shutil.move(filename, category + '/' + filename)
    # print(extension_to_category)


main()
