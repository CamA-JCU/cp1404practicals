"""
CP1404/CP5632 Practical
Sort Files Program V1.0
"""

import os
import shutil


def main():
    """Sort Files Program V1.0."""
    os.chdir('FilesToSort')
    extensions = []
    for filename in os.listdir('.'):
        # find files that don't start with "."
        if not filename[0] == ".":
            extension_starts = filename.find(".") + 1
            extension = filename[extension_starts:]
            if extension not in extensions:
                try:
                    os.mkdir(extension)
                except FileExistsError:
                    pass
                extensions.append(extension)
            shutil.move(filename, extension + '/' + filename)


main()
