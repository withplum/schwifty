import pytest

from schwifty import BIC


def test_bic():
    bic = BIC('GENODEM1GLS')
    assert bic.formatted == 'GENO DE M1 GLS'
    assert bic.validate()


def test_bic_properties():
    bic = BIC('GENODEM1GLS')
    assert bic.length == 11
    assert bic.bank_code == 'GENO'
    assert bic.branch_code == 'GLS'
    assert bic.country_code == 'DE'
    assert bic.location_code == 'M1'


@pytest.mark.parametrize('code', [
    'AAAA',             # Too short
    'AAAADEM1GLSX',     # Too long
    '12ABDEM1GLS',      # Wrong structure in banc-id
    'GENOD1M1GLS',      # Wrong structure in country-code
    'GENOXXM1GLS',      # Wrong country-code
])
def test_invalid_bic(code):
    with pytest.raises(ValueError):
        BIC(code)


def test_bic_from_bank_code():
    bic = BIC.from_bank_code('DE', '43060967')
    assert bic.compact == 'GENODEM1GLS'


def test_bic_from_unknown_bank_code():
    assert not BIC.from_bank_code('PO', '12345678')


def test_magic_methods():
    bic = BIC('GENODEM1GLS')
    assert bic == 'GENODEM1GLS'
    assert bic == BIC('GENODEM1GLS')
    assert bic != BIC('GENODEMMXXX')

    assert str(bic) == 'GENODEM1GLS'
    assert repr(bic) == '<BIC=GENODEM1GLS>'
