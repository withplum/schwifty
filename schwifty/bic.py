from functools import partial
import re

import iso3166

from common import Base
import registry


_bic_re = re.compile(r'[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?')


class BIC(Base):

    def __init__(self, bic, allow_invalid=False):
        super(BIC, self).__init__(bic)
        if not allow_invalid:
            self.validate()

    @classmethod
    def from_bank_code(cls, country_code, bank_code):
        try:
            return cls(registry.get('bank_code')[(country_code, bank_code)]['bic'])
        except KeyError:
            pass

    def validate(self):
        self.validate_length()
        self.validate_structure()
        self.validate_country_code()
        return True

    def validate_length(self):
        if self.length not in (8, 11):
            raise ValueError('Invalid BIC length %d', self.length)

    def validate_structure(self):
        if not _bic_re.match(self.compact):
            raise ValueError('Invalid BIC structure %s', self.compact)

    def validate_country_code(self):
        country_code = self.country_code
        try:
            iso3166.countries_by_alpha2[country_code]
        except KeyError:
            raise ValueError('Invalid country code in BIC %s' % country_code)

    @property
    def formatted(self):
        formatted = ' '.join([self.bank_code, self.country_code, self.location_code])
        if self.branch_code:
            formatted += ' ' + self.branch_code
        return formatted

    bank_code = property(partial(Base._get_component, start=0, end=4))
    branch_code = property(partial(Base._get_component, start=8, end=11))
    country_code = property(partial(Base._get_component, start=4, end=6))
    location_code = property(partial(Base._get_component, start=6, end=8))


registry.build_index('bank', 'bic', 'bic')
registry.build_index('bank', 'bank_code', ('country_code', 'bank_code'))
