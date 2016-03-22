import pytest
from schwifty import IBAN


valid = [
    'AL47 2121 1009 0000 0002 3569 8741',       # Albania
    'AD12 0001 2030 2003 5910 0100',            # Andorra
    'AT61 1904 3002 3457 3201',                 # Austria
    'AZ21 NABZ 0000 0000 1370 1000 1944',       # Republic of Azerbaijan
    'BH67 BMAG 0000 1299 1234 56',              # Bahrain (Kingdom of)
    'BE68 5390 0754 7034',                      # Belgium
    'BA39 1290 0794 0102 8494',                 # Bosnia and Herzegovina
    'BR97 0036 0305 0000 1000 9795 493P 1',     # Brazil
    'BR18 0000 0000 1414 5512 3924 100C 2',     # Brazil
    'BG80 BNBG 9661 1020 3456 78',              # Bulgaria
    'CR05 1520 2001 0262 8406 6',               # Costa Rica
    'HR12 1001 0051 8630 0016 0',               # Croatia
    'CY17 0020 0128 0000 0012 0052 7600',       # Cyprus
    'CZ65 0800 0000 1920 0014 5399',            # Czech Republic
    'CZ94 5500 0000 0010 1103 8930',            # Czech Republic
    'DK50 0040 0440 1162 43',                   # Greenland
    'FO62 6460 0001 6316 34',                   # Faroer
    'GL89 6471 0001 0002 06',                   # Denmark
    'DO28 BAGR 0000 0001 2124 5361 1324',       # Dominican Republic
    'EE38 2200 2210 2014 5685',                 # Estonia
    'FI21 1234 5600 0007 85',                   # Finland
    'FR14 2004 1010 0505 0001 3M02 606',        # France
    'GE29 NB00 0000 0101 9049 17',              # Georgia
    'DE89 3704 0044 0532 0130 00',              # Germany
    'GI75 NWBK 0000 0000 7099 453',             # Gibraltar
    'GR16 0110 1250 0000 0001 2300 695',        # Greece
    'GT82 TRAJ 0102 0000 0012 1002 9690',       # Guatemala
    'HU42 1177 3016 1111 1018 0000 0000',       # Hungary
    'IS14 0159 2600 7654 5510 7303 39',         # Iceland
    'IE29 AIBK 9311 5212 3456 78',              # Ireland
    'IL62 0108 0000 0009 9999 999',             # Israel
    'IT60 X054 2811 1010 0000 0123 456',        # Italy
    'JO94 CBJO 0010 0000 0000 0131 0003 02',    # Jordan
    'KZ86 125K ZT50 0410 0100',                     # Kazakhstan
    'XK05 1212 0123 4567 8906',                 # Republic of Kosovo
    'KW81 CBKU 0000 0000 0000 1234 5601 01',    # Kuwait
    'LV80 BANK 0000 4351 9500 1',               # Latvia
    'LB62 0999 0000 0001 0019 0122 9114',       # Lebanon
    'LI21 0881 0000 2324 013A A',               # Liechtenstein (Principality of)
    'LT12 1000 0111 0100 1000',                 # Lithuania
    'LU28 0019 4006 4475 0000',                 # Luxembourg
    'MK07 2501 2000 0058 984',                  # Macedonia, Former Yugoslav Republic of
    'MT84 MALT 0110 0001 2345 MTLC AST0 01S',   # Malta
    'MR13 0002 0001 0100 0012 3456 753',        # Mauritania
    'MU17 BOMM 0101 1010 3030 0200 000M UR',    # Mauritius
    'MD24 AG00 0225 1000 1310 4168',            # Moldova
    'MC58 1122 2000 0101 2345 6789 030',        # Monaco
    'ME25 5050 0001 2345 6789 51',              # Montenegro
    'NL91 ABNA 0417 1643 00',                   # The Netherlands
    'NO93 8601 1117 947',                       # Norway
    'PK36 SCBL 0000 0011 2345 6702',            # Pakistan
    'PS92 PALS 0000 0000 0400 1234 5670 2',     # Palestine, State of
    'PL61 1090 1014 0000 0712 1981 2874',       # Poland
    'PT50 0002 0123 1234 5678 9015 4',          # Portugal
    'QA58 DOHB 0000 1234 5678 90AB CDEF G',     # Qatar
    'RO49 AAAA 1B31 0075 9384 0000',            # Romania
    # 'LC62 HEMM 0001 0001 0012 0012 0002 3015',  # Saint Lucia
    'SM86 U032 2509 8000 0000 0270 100',        # San Marino
    'ST68 0001 0001 0051 8453 1011 2',          # Sao Tome And Principe
    'SA03 8000 0000 6080 1016 7519',            # Saudi Arabia
    'RS35 2600 0560 1001 6113 79',              # Serbia
    # 'SC25 SSCB1101 0000 0000 0000 1497 USD',    # Seychelles
    'SK31 1200 0000 1987 4263 7541',            # Slovak Republic
    'SI56 1910 0000 0123 438',                  # Slovenia
    'ES91 2100 0418 4502 0005 1332',            # Spain
    'SE45 5000 0000 0583 9825 7466',            # Sweden
    'CH93 0076 2011 6238 5295 7',               # Switzerland
    'TL38 0080 0123 4567 8910 157',             # Timor-Leste
    'TN59 1000 6035 1835 9847 8831',            # Tunisia
    'TR33 0006 1005 1978 6457 8413 26',         # Turkey
    'UA21 3996 2200 0002 6007 2335 6600 1',     # Ukraine
    'AE07 0331 2345 6789 0123 456',             # United Arab Emirates
    'GB29 NWBK 6016 1331 9268 19',              # United Kingdom
    'VG96 VPVG 0000 0123 4567 8901',            # Virgin Islands, British
]


invalid = [
    'DE89 3704 0044 0532 0130',                 # Too short
    'DE89 3704 0044 0532 0130 0000',            # Too long
    'XX89 3704 0044 0532 0130 00',              # Wrong country-code
    'DE99 3704 0044 0532 0130 00',              # Wrong check digits
    'DEAA 3704 0044 0532 0130 00',              # Wrong format (check digits)
    'DE89 AA04 0044 0532 0130 00',              # Wrong format (country specific)
]


@pytest.mark.parametrize('number', valid)
def test_parse_iban(number):
    iban = IBAN(number)
    assert iban.formatted == number


@pytest.mark.parametrize('number', invalid)
def test_parse_iban_allow_invalid(number):
    iban = IBAN(number, allow_invalid=True)
    with pytest.raises(ValueError):
        iban.validate()


@pytest.mark.parametrize('number', invalid)
def test_invalid_iban(number):
    with pytest.raises(ValueError):
        IBAN(number)


def test_iban_properties():
    iban = IBAN('DE42430609677000534100')
    assert iban.bank_code == '43060967'
    assert iban.branch_code == ''
    assert iban.account_code == '7000534100'
    assert iban.country_code == 'DE'
    assert iban.bic == 'GENODEM1GLS'
    assert iban.formatted == 'DE42 4306 0967 7000 5341 00'
    assert iban.length == 22


@pytest.mark.parametrize('components,compact', [
    (('DE', '43060967', '7000534100'), 'DE42430609677000534100'),
    (('DE', '51230800', '2622196545'), 'DE61512308002622196545'),
    (('DE', '20690500', '9027378'), 'DE37206905000009027378'),
    (('DE', '75090900', '7408418'), 'DE04750909000007408418')
])
def test_generate_iban(components, compact):
    iban = IBAN.generate(*components)
    assert iban.compact == compact


@pytest.mark.parametrize('country_code,bank_code,account_code', [
    ('DE', '012345678', '7000123456'),
    ('DE', '51230800', '01234567891'),
])
def test_generate_iban_invalid(country_code, bank_code, account_code):
    with pytest.raises(ValueError):
        IBAN.generate(country_code, bank_code, account_code)


def test_magic_methods():
    iban = IBAN('DE42430609677000534100')
    assert iban == 'DE42430609677000534100'
    assert iban == IBAN('DE42430609677000534100')
    assert iban != IBAN('ES9121000418450200051332')
    assert iban < IBAN('ES9121000418450200051332')

    assert str(iban) == 'DE42430609677000534100'
    assert repr(iban) == '<IBAN=DE42430609677000534100>'
