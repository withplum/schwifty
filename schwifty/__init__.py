try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version  # type: ignore

from schwifty.bic import BIC
from schwifty.iban import IBAN


__all__ = ["IBAN", "BIC"]
__version__ = version(__name__)
