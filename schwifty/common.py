import re


_clean_regex = re.compile(r'\s+')


class Base(object):

    def __init__(self, code):
        self._code = clean(code)

    def __str__(self):
        return self.compact

    def __repr__(self):
        return '<%s=%s>' % (self.__class__.__name__, str(self))

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        elif isinstance(other, self.__class__):
            return str(self) == str(other)
        return False

    @property
    def compact(self):
        return self._code

    @property
    def length(self):
        return len(self.compact)

    def _get_component(self, start, end=None):
        if start < self.length and (end is None or end <= self.length):
            return self.compact[start:end] if end else self.compact[start:]


def clean(string):
    return _clean_regex.sub('', string).upper()
