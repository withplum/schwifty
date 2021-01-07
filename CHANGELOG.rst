.. _changelog:

Changelog
=========

Versions follow `CalVer <http://www.calver.org/>`_ with the scheme ``YY.0M.Micro``.

Unreleased
----------

Changed
~~~~~~~
* Restructure documentation and change theme to `furo <https://pradyunsg.me/furo/>`_.


2020.08.3 - 2020/08/31
----------------------

Fixed
~~~~~
* Fixed IBAN generation for countries with branch/sort code
* Add generated banks for Spain

2020.08.2 - 2020/08/30
----------------------

Fixed
~~~~~
* Poland's IBAN spec only has a branch-code but no bank-code
* Fixed listing of supported countries for BIC derivation.
* Fixed bank registry for Hungary.

Changed
~~~~~~~
* Updated bank registry Poland, Belgium and Austria.
* Updated IBAN spec for Sao Tome and Principe

2020.08.1 - 2020/08/28
----------------------

Added
~~~~~
* New attribute :class:`.BIC.is_valid` and :class:`.IBAN.is_valid`.

2020.08.0 - 2020/08/06
----------------------

Changed
~~~~~~~
* Updated bank registry for Poland.

2020.05.3 - 2020/05/25
----------------------

Added
~~~~~
* Added banks for France, Switzerland and Great Britain.

2020.05.2 - 2020/05/08
----------------------

Added
~~~~~
* Added :attr:`.BIC.country` and :attr:`.IBAN.country`.
