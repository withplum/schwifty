import string
from functools import partial

from schwifty import checksum
from schwifty import registry


alphabet: str = string.digits + string.ascii_uppercase


register = partial(checksum.register, prefix="IT")


@register
class DefaultAlgorithm(checksum.Algorithm):
    name = "default"
    accepts = checksum.InputType.BBAN
    checksum_length = 1

    def compute(self, bban: str) -> str:
        spec = registry.get("iban")
        assert isinstance(spec, dict)

        odds = (
            [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2]
            + [4, 18, 20, 11, 3, 6, 8, 12, 14, 16]
            + [10, 22, 25, 24, 23, 27, 28, 26]
        )
        sum_ = 0
        for i, char in enumerate(bban[self.checksum_length - spec["IT"]["bban_length"] :]):
            if (i + 1) % 2 == 0:
                sum_ += alphabet.index(char)
            else:
                sum_ += odds[alphabet.index(char)]
        return alphabet[sum_ % 26 + 10]

    def validate(self, bban: str) -> bool:
        return bban[0] == self.compute(bban[self.checksum_length :])
