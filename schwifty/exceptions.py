class SchwiftyException(ValueError):
    """Base exception of all schwifty related errors."""


class InvalidLength(SchwiftyException):
    """Indicates that the length of the input does not match the specifcation."""


class InvalidStructure(SchwiftyException):
    """Indicates a strctural error of the input (e.g. invalid characters)."""


class InvalidCountryCode(SchwiftyException):
    """Unknown country code in the input."""


class InvalidBankCode(SchwiftyException):
    """Indicates that the bank code has an invalid structure."""


class InvalidBranchCode(SchwiftyException):
    """Indicates that the branch code has an invalid strucutre."""


class InvalidAccountCode(SchwiftyException):
    """Indicates that the account code has an invalid strucutre."""


class InvalidChecksumDigits(SchwiftyException):
    """Indicates that the IBAN's checksum is invalid."""


class InvalidBBANChecksum(SchwiftyException):
    """Indicates that the BBAN's checksum is invalid."""
