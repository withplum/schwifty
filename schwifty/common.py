import re
from functools import total_ordering
from typing import Any
from typing import Optional


_clean_regex = re.compile(r"\s+")


@total_ordering
class Base:
    def __init__(self, code: str) -> None:
        self._code = clean(code)

    def __str__(self) -> str:
        return self.compact

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}={self!s}>"

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        return str(self) == str(other)

    def __lt__(self, other: Any) -> bool:
        return str(self) < str(other)

    @property
    def compact(self) -> str:
        """str: Compact representation of the code."""
        return self._code

    @property
    def length(self) -> int:
        """int: Length of the compact code."""
        return len(self.compact)

    def _get_component(self, start: int, end: Optional[int] = None) -> str:
        if start < self.length and (end is None or end <= self.length):
            return self.compact[start:end] if end else self.compact[start:]
        return ""


def clean(s: str) -> str:
    return _clean_regex.sub("", s).upper()
