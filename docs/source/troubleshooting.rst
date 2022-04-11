Troubleshooting
===============

UnicodeDecodeError on import
----------------------------

Since ``schwifty``'s bank regisry contains bank names with non-ASCII characters, the corresponding
JSON files are encoded in UTF-8. In some Docker container setups (and possibly elsewhere) it might
occur that a ``UnicodeDecodeError`` is raised on import. This can be fixed in most cases by
adjusting the locales setup to support UTF-8. See `this blog post
<http://jaredmarkell.com/docker-and-locales/>`_ for more information. Since version ``2022.04.0``
this issue has been fixed, so that ``schwifty`` uses the correct encoding by default.
