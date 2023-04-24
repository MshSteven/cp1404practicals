"""
estimate time: 20 minutes
actual time: 20 minutes
"""


class ProgrammingLanguage:
    """Represent a programming language object."""
    def __init__(self, name="", typing="Dynamic", reflection=True, year=0):
        """
        name: name of programming language
        typing: type of programming language
        reflection: reflection of programming language
        year: created year of programming language
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine is the programming language dynamic or static."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """format string of display programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appear in {self.year}"
