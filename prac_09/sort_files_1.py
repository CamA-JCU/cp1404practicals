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
        print(filename)
        extension_starts = filename.find(".") + 1
        print(extension_starts)
        extension = filename[extension_starts:]
        print(extension)
        extensions.append(extension)
    print(extensions)


main()
