import functools

from schwifty import checksum


register = functools.partial(checksum.register, prefix="BE")


@register
class DefaultAlgorithm(checksum.Algorithm):
    name = "default"
    accepts = checksum.InputType.BBAN

    def compute(self, bban: str) -> str:
        return str(int(bban[:-2]) % 97)

    def validate(self, bban: str) -> bool:
        return bban[-2:] == self.compute(bban)
