"""
CP1404/CP5632 Practical
Clean Up files program
"""

import os


SEPARATOR = "_"


def main():
    """Clean Up files program."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", SEPARATOR).replace(".TXT", ".txt")
    new_name = ""
    for i, char in enumerate(filename):
        if not filename[i - 1].isalpha() and filename[i - 1] != "." and filename[i - 1] != "'" and char.islower():
            new_name += char.upper()
        elif char == "." and i != len(filename) - 4:
            pass
        else:
            new_name += char
        try:
            if (filename[i + 1].isupper() or filename[i + 1] == "(") and char.isalpha():
                new_name += SEPARATOR
        except IndexError:
            pass
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            filename = os.path.join(directory_name, filename)
            os.rename(filename, new_name)

# main()


demo_walk()

