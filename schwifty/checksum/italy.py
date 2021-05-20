import string
from functools import partial

from schwifty import checksum


_alphabet: str = string.digits + string.ascii_uppercase


register = partial(checksum.register, prefix="IT")


@register
class DefaultAlgorithm(checksum.Algorithm):
    name = "default"
    accepts = checksum.InputType.BBAN

    def compute(self, bban: str) -> str:
        odds = (
            [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2]
            + [4, 18, 20, 11, 3, 6, 8, 12, 14, 16]
            + [10, 22, 25, 24, 23, 27, 28, 26]
        )
        sum_ = 0
        for i, char in enumerate(bban):
            if (i + 1) % 2 == 0:
                sum_ += _alphabet.index(char)
            else:
                sum_ += odds[_alphabet.index(char)]
        return _alphabet[sum_ % 26 + 10]

    def validate(self, bban: str) -> bool:
        return bban[0] == self.compute(bban[1:])
