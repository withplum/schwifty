import functools

from schwifty import checksum
from schwifty import registry


register = functools.partial(checksum.register, prefix="FR")

numerics = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "1",
    "B": "2",
    "C": "3",
    "D": "4",
    "E": "5",
    "F": "6",
    "G": "7",
    "H": "8",
    "I": "9",
    "J": "1",
    "K": "2",
    "L": "3",
    "M": "4",
    "N": "5",
    "O": "6",
    "P": "7",
    "Q": "8",
    "R": "9",
    "S": "2",
    "T": "3",
    "U": "4",
    "V": "5",
    "W": "6",
    "X": "7",
    "Y": "8",
    "Z": "9",
}


def convert(code: str) -> int:
    res = ""
    for c in code:
        res += numerics[c]
    return int(res)


@register
class DefaultAlgorithm(checksum.Algorithm):
    name = "default"
    accepts = checksum.InputType.BBAN
    checksum_length = 2

    def compute(self, bban: str) -> str:
        spec = registry.get("iban")
        assert isinstance(spec, dict)

        positions = spec["FR"]["positions"]
        bank_code = bban[slice(*positions["bank_code"])]
        branch_code = bban[slice(*positions["branch_code"])]
        account_code = bban[slice(*positions["account_code"])]

        checksum = 97 - (
            (89 * convert(bank_code) + 15 * convert(branch_code) + 3 * convert(account_code)) % 97
        )
        return str(checksum).zfill(self.checksum_length)

    def validate(self, bban: str) -> bool:
        return bban[-self.checksum_length :] == self.compute(bban[: -self.checksum_length])
