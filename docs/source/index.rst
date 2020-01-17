Get schwifty with IBANs and BICs
================================

Schwifty is a Python library that let's you easily work with IBANs and BICs as specified by the ISO.
IBAN is the Internation Bank Account Number and BIC the Business Identifier Code. Both are used for
international money transfer.

Features
--------

Schwifty lets you

* validate check-digits and the country specific format of IBANs
* validate format and country codes from BICs
* generate BICs from bank-codes (works for Germany for now)
* generate IBANs from country-code, bank-code and account-number.
* access all relevant components as attributes


Examples
--------


Basic usage
~~~~~~~~~~~

Consider the following code example for :class:`IBAN`-objects:

.. code-block:: python

  >>> from schwifty import IBAN
  >>> iban = IBAN('DE89 3704 0044 0532 0130 00')
  >>> iban.compact
  'DE89370400440532013000'
  >>> iban.formatted
  'DE89 3704 0044 0532 0130 00'
  >>> iban.country_code
  'DE'
  >>> iban.bank_code
  '37040044'
  >>> iban.account_code
  '0532013000'
  >>> iban.length
  22
  >>> iban.bic
  <BIC=COBADEFFXXX>

or for working with :class:`BIC`-objects

.. code-block:: python

  >>> from schwifty import BIC
  >>> bic = BIC('PBNKDEFFXXX')
  >>> bic.bank_code
  'PBNK'
  >>> bic.branch_code
  'XXX'
  >>> bic.country_code
  'DE'
  >>> bic.location_code
  'FF'
  >>> bic.domestic_bank_codes
  ['10010010',
   '20010020',
   ...
   '86010090']


Validation
~~~~~~~~~~

When it comes to validation the :class:`IBAN` and :class:`BIC` constructors raise a ``ValueError``
whenever the provided code is incorrect for some reason:

.. code-block:: python

  >>> IBAN('DX89 3704 0044 0532 0130 00')
  ...
  ValueError: Unknown country-code DX

  >>> IBAN('DE99 3704 0044 0532 0130 00')
  ...
  ValueError: Invalid checksum digits

  >>> BIC('PBNKDXFFXXX')
  ...
  ValueError: Invalid country code DX

  >>> BIC('PBNKDXFFXXXX')
  ...
  ValueError: Invalid length 12

  >>> BIC('PBN1DXFFXXXX')
  ...
  ValueError: Invalid structure PBN1DXFFXXXX


Generation
~~~~~~~~~~

You can generate :class:`IBAN`-objects from country-code, bank-code and account-number by using the
:meth:`IBAN.generate()`-method. It will automatically calculate the correct checksum digits for you.

.. code-block:: python

  >>> iban = IBAN.generate('DE', bank_code='10010010', account_code='12345')
  <IBAN=DE40100100100000012345>
  >>> iban.checksum_digits
  '40'

For german banks you can also generate :class:`BIC`-objects from local bank-codes

.. code-block:: python

  >>> bic = BIC.from_bank_code('DE', '43060967')
  >>> bic.formatted
  'GENO DE M1 GLS'


API documentation
-----------------
.. toctree::
   :maxdepth: 2

   api
