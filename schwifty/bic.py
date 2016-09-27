from functools import partial
import re

import iso3166

from schwifty.common import Base
from schwifty import registry


_bic_re = re.compile(r'[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?')


class BIC(Base):
    """The BIC object.

    Examples:

        You can either create a new BIC object by providing a code as text::

            >>> bic = BIC('GENODEM1GLS')
            >>> bic.country_code
            'DE'
            >>> bic.location_code
            'M1'
            >>> bic.bank_code
            'GENO'

        or by using the :meth:`from_bank_code` classmethod::

            >>> bic = BIC.from_bank_code('DE', '43060967')
            >>> bic.formatted
            'GENO DE M1 GLS'
    Args:
        bic (str): The BIC number.
        allow_invalid (bool): If set to ``True`` validation is skipped on instantiation.
    """

    def __init__(self, bic, allow_invalid=False):
        super(BIC, self).__init__(bic)
        if not allow_invalid:
            self.validate()

    @classmethod
    def from_bank_code(cls, country_code, bank_code):
        """Create a new BIC object from country- and bank-code.

        Args:
            country_code (str): ISO 3166 alpha2 country-code.
            bank_code (str): Country specific bank-code.

        Note:
            This currently only works for German bank-codes.
        """
        try:
            return cls(registry.get('bank_code')[(country_code, bank_code)]['bic'])
        except KeyError:
            pass

    def validate(self):
        self._validate_length()
        self._validate_structure()
        self._validate_country_code()
        return True

    def _validate_length(self):
        if self.length not in (8, 11):
            raise ValueError("Invalid length '{}'".format(self.length))

    def _validate_structure(self):
        if not _bic_re.match(self.compact):
            raise ValueError("Invalid structure '{}'".format(self.compact))

    def _validate_country_code(self):
        country_code = self.country_code
        try:
            iso3166.countries_by_alpha2[country_code]
        except KeyError:
            raise ValueError("Invalid country code '{}'".format(country_code))

    @property
    def formatted(self):
        """str: The BIC separated in the blocks bank-, country- and location-code."""
        formatted = ' '.join([self.bank_code, self.country_code, self.location_code])
        if self.branch_code:
            formatted += ' ' + self.branch_code
        return formatted

    @property
    def country_bank_code(self):
        """str or None: The country specific bank-code associated to the BIC."""
        entry = registry.get('bic').get(self.compact)
        if entry:
            return entry.get('bank_code')

    @property
    def exists(self):
        """bool: Indicates if the BIC is available in Schwifty's registry."""
        return bool(registry.get('bic').get(self.compact))

    @property
    def type(self):
        """Indicates the type of BIC.

        This can be one of 'testing', 'passive', 'reverse billing' or 'default'

        Returns:
            str: The BIC type.
        """
        if self.location_code[1] == '0':
            return 'testing'
        elif self.location_code[1] == '1':
            return 'passive'
        elif self.location_code[1] == '2':
            return 'reverse billing'
        else:
            return 'default'

    bank_code = property(partial(Base._get_component, start=0, end=4),
                         doc="str: The bank-code part of the BIC.")
    branch_code = property(partial(Base._get_component, start=8, end=11),
                           doc="str or None: The branch-code part of the BIC (if available)")
    country_code = property(partial(Base._get_component, start=4, end=6),
                            doc="str: The ISO 3166 alpha2 country-code.")
    location_code = property(partial(Base._get_component, start=6, end=8),
                             doc="str: The location code of the BIC.")


registry.build_index('bank', 'bic', 'bic')
registry.build_index('bank', 'bank_code', ('country_code', 'bank_code'), primary=True)
