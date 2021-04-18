"""CP1404/CP5632 Practical - Programming language."""


class ProgrammingLanguage:
    """Represent a Programming Language."""

    def __init__(self, typing="", reflection="", year=0):
        """Initialise a Programming Language instance."""

        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if language is dyanmic."""
        return self.typing == "Dyanmic"
