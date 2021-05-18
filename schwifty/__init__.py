from importlib.metadata import version

from schwifty.bic import BIC
from schwifty.iban import IBAN


__all__ = ["IBAN", "BIC"]
__version__ = version(__name__)
