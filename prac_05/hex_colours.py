"""
CP1404/CP5632 Practical
Hex Colours in a dictionary
"""

COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
           "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "BlanchedAlmond": "#ffebcd",
           "blue1": "#0000ff", "BlueViolet": "#8a2be2", "brown": "#a52a2a"}

colour = input("Colour: ")
while colour != "":
    try:
        print(COLOURS[colour])
    except KeyError:
        print("Colour not found")
    colour = input("Colour: ")
