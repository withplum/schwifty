.. _changelog:

Changelog
=========

Versions follow `CalVer <http://www.calver.org/>`_ with the scheme ``YY.0M.Micro``.

`2021.05.2`_ - 2021/05/23
-------------------------

Added
~~~~~
* Country specifc checksum validation for Belgian banks, as well as support for generating the
  checksum when using the :meth:`IBAN.generate`-method. `@mhemeryck <https://github.com/mhemeryck>`_

`2021.05.1`_ - 2021/05/20
-------------------------

Added
~~~~~
* The IBAN validation now optionally includes the verification of the country specific checksum
  within the BBAN. This currently works for German and Italian banks. For German banks the checksum
  algorithm for the account code is chosen by the bank code. Since there are over 150 bank specific
  algorithms in Germany not all of them are implemented at the moment, but the majority of banks should
  be covered.

Changed
~~~~~~~
* Update bank registry for Germany, Poland, Czech Republic, Austria and Netherlands.

`2021.05.0`_ - 2021/05/02
-------------------------

Added
~~~~~
* Added manually curated list of Lithuanian Banks (e.g Revolut Payments UAB).

`2021.04.0`_ - 2021/04/23
-------------------------

Changed
~~~~~~~
* Added type hints to the entire code base.
* Dropped support for Python 3.6
* Update bank registry for Austria, Poland, Germany, Belgium, Czech Republic, Netherlands, Slovenia and Slovakia.

`2021.01.0`_ - 2021/01/20
-------------------------

Changed
~~~~~~~
* Restructure documentation and change theme to `furo <https://pradyunsg.me/furo/>`_.
* Added dedicated exception classes for various validation errors.
* Drop support for Python 2. Only Python 3.6+ will be supported from now on.
* Use PEP 517/518 compliant build setup.

`2020.11.0`_ - 2020/12/02
-------------------------

Changed
~~~~~~~
* Updated IBAN registry and bank registries of Poland, Germany, Austria, Belgium, Netherlands,
  Czech Republic and Slovenia.

Added
~~~~~
* Added generated banks for Slovakia `@petrboros <https://github.com/petrboros>`_.
* Added a test to validate the correctnes of BICs in the registry `@ckoehn <https://github.com/ckoehn>`_.

Fixed
~~~~~
* Fixed encoding for Polish bank registry `@michal-michalak <https://github.com/michal-michalak>`_.

`2020.09.0`_ - 2020/09/07
-------------------------

Changed
~~~~~~~
* Migrated build and test pipelines to GitHub actions.

Added
~~~~~
* Added generated banks for Netherlands `@insensitiveclod <https://github.com/insensitiveclod>`_.
* Added generated banks for Spain.

`2020.08.3`_ - 2020/08/31
-------------------------

Fixed
~~~~~
* Fixed IBAN generation for countries with branch/sort code
* Add generated banks for Spain

`2020.08.2`_ - 2020/08/30
-------------------------

Fixed
~~~~~
* Poland's IBAN spec only has a branch-code but no bank-code
* Fixed listing of supported countries for BIC derivation.
* Fixed bank registry for Hungary.

Changed
~~~~~~~
* Updated bank registry Poland, Belgium and Austria.
* Updated IBAN spec for Sao Tome and Principe

`2020.08.1`_ - 2020/08/28
-------------------------

Added
~~~~~
* New attribute :class:`.BIC.is_valid` and :class:`.IBAN.is_valid`.

`2020.08.0`_ - 2020/08/06
-------------------------

Changed
~~~~~~~
* Updated bank registry for Poland.

`2020.05.3`_ - 2020/05/25
-------------------------

Added
~~~~~
* Added banks for France, Switzerland and Great Britain.

`2020.05.2`_ - 2020/05/08
-------------------------

Added
~~~~~
* Added :attr:`.BIC.country` and :attr:`.IBAN.country`.


.. _2021.05.2: https://github.com/mdomke/schwifty/compare/2021.05.1...2021.05.2
.. _2021.05.1: https://github.com/mdomke/schwifty/compare/2021.05.0...2021.05.1
.. _2021.05.0: https://github.com/mdomke/schwifty/compare/2021.04.0...2021.05.0
.. _2021.04.0: https://github.com/mdomke/schwifty/compare/2021.01.0...2021.04.0
.. _2021.01.0: https://github.com/mdomke/schwifty/compare/2020.11.0...2021.01.0
.. _2020.11.0: https://github.com/mdomke/schwifty/compare/2020.09.0...2020.11.0
.. _2020.09.0: https://github.com/mdomke/schwifty/compare/2020.08.3...2020.09.0
.. _2020.08.3: https://github.com/mdomke/schwifty/compare/2020.08.2...2020.08.3
.. _2020.08.2: https://github.com/mdomke/schwifty/compare/2020.08.1...2020.08.2
.. _2020.08.1: https://github.com/mdomke/schwifty/compare/2020.08.0...2020.08.1
.. _2020.08.0: https://github.com/mdomke/schwifty/compare/2020.05.3...2020.08.0
.. _2020.05.3: https://github.com/mdomke/schwifty/compare/2020.05.2...2020.05.3
.. _2020.05.2: https://github.com/mdomke/schwifty/compare/2020.05.1...2020.05.2
