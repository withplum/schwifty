class SchwiftyException(ValueError):
    pass


class InvalidLength(SchwiftyException):
    pass


class InvalidStructure(SchwiftyException):
    pass


class InvalidCountryCode(SchwiftyException):
    pass


class InvalidBankCode(SchwiftyException):
    pass


class InvalidBranchCode(SchwiftyException):
    pass


class InvalidAccountCode(SchwiftyException):
    pass


class InvalidChecksumDigits(SchwiftyException):
    pass
