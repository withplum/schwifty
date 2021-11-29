import functools

from schwifty import checksum
from schwifty import registry


register = functools.partial(checksum.register, prefix="FR")

CONVERT_LETTERS = {
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
              'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9',
              'J': '1', 'K': '2', 'L': '3', 'M': '4', 'N': '5', 'O': '6', 'P': '7', 'Q': '8', 'R': '9',
                        'S': '2', 'T': '3', 'U': '4', 'V': '5', 'W': '6', 'X': '7', 'Y': '8', 'Z': '9',
}

@register
class DefaultAlgorithm(checksum.Algorithm):
    name = "default"
    accepts = checksum.InputType.BBAN
    checksum_length = 2

    def compute(self, bban: str) -> str:
        spec = registry.get("iban")
        assert isinstance(spec, dict)
        bank_code = bban[spec["FR"]["positions"]["bank_code"][0]:spec["FR"]["positions"]["bank_code"][1]]
        branch_code = bban[spec["FR"]["positions"]["branch_code"][0]:spec["FR"]["positions"]["branch_code"][1]]
        account_code = bban[spec["FR"]["positions"]["account_code"][0]:spec["FR"]["positions"]["account_code"][1]]

        num_bank_code = ''
        for bank_code_char in bank_code:
            num_bank_code = num_bank_code + CONVERT_LETTERS[bank_code_char]

        num_branch_code = ''
        for branch_code_char in branch_code:
            num_branch_code = num_branch_code + CONVERT_LETTERS[branch_code_char]

        num_account_code = ''
        for account_code_char in account_code:
            num_account_code = num_account_code + CONVERT_LETTERS[account_code_char]

        checksum = 97 -((89 * int(num_bank_code) + 15 * int(num_branch_code) + 3 * int(num_account_code)) % 97)
        return str(checksum).zfill(self.checksum_length)

    def validate(self, bban: str) -> bool:
        return bban[-self.checksum_length :] == self.compute(bban[: -self.checksum_length])
