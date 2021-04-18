"""CP1404/CP5632 Practical - Programming language."""


class ProgrammingLanguage:
    """Represent a Programming Language."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of ProgrammingLanguage object."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.is_dynamic(), self.year)

    def is_dynamic(self):
        """Determine if language is dynamic."""
        return self.typing == "Dynamic"
