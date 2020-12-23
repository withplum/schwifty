.. image:: https://img.shields.io/pypi/v/schwifty.svg?style=flat-square
    :target: https://pypi.python.org/pypi/schwifty
.. image:: https://img.shields.io/github/workflow/status/mdomke/schwifty/lint-and-test?style=flat-square
    :target: https://github.com/mdomke/schwifty/actions?query=workflow%3Alint-and-test
.. image:: https://img.shields.io/pypi/l/schwifty.svg?style=flat-square
    :target: https://pypi.python.org/pypi/schwifty
.. image:: https://readthedocs.org/projects/schwifty/badge/?version=latest&style=flat-square
    :target: https://schwifty.readthedocs.io
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square
    :target: https://black.readthedocs.io/en/stable/index.html


Gotta get schwifty with your IBANs
==================================

.. teaser-begin

``schwifty`` is a Python library that let's you easily work with IBANs and BICs
as specified by the ISO. IBAN is the Internation Bank Account Number and BIC
the Business Identifier Code. Both are used for international money transfer.

Features
--------

``schwifty`` lets you

* validate check-digits and the country specific format of IBANs
* validate format and country codes from BICs
* generate BICs from country and bank-code
* generate IBANs from country-code, bank-code and account-number.
* get the BIC associated to an IBAN's bank-code
* access all relevant components as attributes

.. teaser-end

Versioning
----------

Since the IBAN specification and the mapping from BIC to bank_code is updated from time to time,
``schwifty`` uses `CalVer <http://www.calver.org/>`_ for versioning with the scheme ``YY.0M.Micro``.

.. examples-begin

Examples
--------

Basic Usage
~~~~~~~~~~~

Consider the following code example for :class:`.IBAN`-objects:

.. code-block:: pycon

  >>> from schwifty import IBAN
  >>> iban = IBAN('DE89 3704 0044 0532 0130 00')
  <IBAN=DE89370400440532013000>
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

After creating an :class:`.IBAN`-object you can access all relevant components as attributes. For some
countries it is also possible to get ahold of the :class:`.BIC` associated to the bank-code of the IBAN.

A BIC is a unique identification code for both financial and non-financial institutes. ``schwifty``
provides a :class:`.BIC``-object, that has a similar interface to the :class:`.IBAN`.

.. code-block:: pycon

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

The :attr:`.BIC.domestic_bank_codes` lists the country specific bank codes as you can find them as
part of the IBAN. This mapping is part of a manually curated registry that ships with ``schwifty``
and is not available for all countries.


Validation
~~~~~~~~~~

When it comes to validation the :class:`.IBAN` and :class:`.BIC` constructors raise a ``ValueError``
whenever the provided code is incorrect for some reason.

For IBANs - with respect to ISO 13616 compliance - it is checked if the account-code, the bank-code
and possibly the branch-code have the correct country-specific format. E.g.:

.. code-block:: pycon

  >>> IBAN('DX89 3704 0044 0532 0130 00')
  ...
  ValueError: Unknown country-code DX

  >>> IBAN('DE99 3704 0044 0532 0130 00')
  ...
  ValueError: Invalid checksum digits


For BICs it is checked if the country-code and the length is valid and if the structure matches the
ISO 9362 specification.

.. code-block:: pycon

  >>> BIC('PBNKDXFFXXX')
  ...
  ValueError: Invalid country code DX

  >>> BIC('PBNKDXFFXXXX')
  ...
  ValueError: Invalid length 12

  >>> BIC('PBN1DXFFXXXX')
  ...
  ValueError: Invalid structure PBN1DXFFXXXX

If catching a ``ValueError`` would complicate your code flow you can also use the
:attr:`.IBAN.is_valid` property. E.g.:

.. code-block:: python

  if IBAN(value, allow_invalid=True).is_valid:
    # do something with value


Generation
~~~~~~~~~~

You can generate :class:`.IBAN`-objects from country-code, bank-code and
account-number by using the
:meth:`.IBAN.generate()`-method. It will automatically calculate the correct checksum digits for you.

.. code-block:: pycon

  >>> iban = IBAN.generate('DE', bank_code='10010010', account_code='12345')
  <IBAN=DE40100100100000012345>
  >>> iban.checksum_digits
  '40'

Notice that even that the account-code has less digits than required (in Germany accounts should be
10 digits long), zeros have been added at the correct location.

For some countries you can also generate :class:`.BIC`-objects from local
bank-codes, e.g.:

.. code-block:: pycon

  >>> bic = BIC.from_bank_code('DE', '43060967')
  >>> bic.formatted
  'GENO DE M1 GLS'

.. examples-end


.. installation-begin

Installation
------------

To install ``schwifty``, simply:

.. code-block:: bash

  $ pip install schwifty

.. installation-end


Development
-----------

We use the `black`_ as code formatter. This avoids discussions about style preferences in the same
way as ``gofmt`` does the job for Golang. The conformance to the formatting rules is checked in the
CI pipeline, so that it is recommendable to install the configured `pre-commit`_-hook, in order to
avoid long feedback-cycles.

.. code-block:: bash

   $ pre-commit install

You can also use the ``fmt`` Makefile-target to format the code or use one of the available `editor
integrations`_.


Name
----

Since ``swift`` and ``swiftly`` were already taken by the OpenStack-project, but we somehow wanted
to point out the connection to SWIFT, Rick and Morty came up with the idea to name the project
``schwifty``.

.. image:: https://i.cdn.turner.com/adultswim/big/video/get-schwifty-pt-2/rickandmorty_ep205_002_vbnuta15a755dvash8.jpg


.. _black:  https://black.readthedocs.io/en/stable/index.html
.. _pre-commit: https://pre-commit.com
.. _editor integrations:  https://black.readthedocs.io/en/stable/editor_integration.html
