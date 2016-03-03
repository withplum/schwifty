Gotta get schwifty with your IBANs
==================================


Schwifty is a Python library for working with BICs and IBANs. It allows you to

* validate check-digits and the country specific format of IBANs
* validate format and country codes from BICs
* generate BICs from bank-codes (works for Germany for now)
* generate IBANs from country-code, bank-code and account-number.
* access all relevant components as attributes


Usage
-----

Let's jump right into it:

.. code-block:: python

  >>> from schwifty import IBAN
  >>> iban = IBAN('DE89 3704 0044 0532 0130 00')
  >>> iban.compact
  'DE89 3704 0044 0532 0130 00'
  >>> iban.country_code
  'DE'
  >>> iban.bank_code
  '37040044'
  >>> iban.account_code
  '0532013000'
  >>> iban.length
  22



Installation
------------

To install Schwifty, simply:

.. code-block:: bash

  $ pip install schwifty

