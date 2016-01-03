What is font-unicode?
---------------------

font-unicode is a command line application that performs searches for
Unicode character names by Unicode code points, and for Unicode code
points by character names. It supports the Unicode standard v8.0.0. The
query results are supplemented with the Adobe Glyph List for New Fonts
v1.7 glyph names where applicable.

Install
-------

Install with ``pip`` using the command:

::

    $ pip install font-unicode

or `download the source
repository <https://github.com/source-foundry/font-unicode/tarball/master>`__,
unpack it, and navigate to the top level of the repository. Then enter:

::

    $ python setup.py install

Usage
-----

Search by Unicode Code Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ font-unicode search [Unicode code point 1] [...Unicode code point X]

You can use either the ``u+0000`` or ``0000`` format for the Unicode
code point queries. Include one or more queries to the ``search``
command.

Search by Unicode Character Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ font-unicode name [Unicode character name query 1] [...Unicode character name query X]

Include one or more character name search terms as arguments to the
``name`` command. Surround multi-word queries with quotes. You can
include multiple searches in the same command.

Pipe Raw Data to Another Executable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can pipe the raw `Adobe Glyph List for New
Fonts <https://raw.githubusercontent.com/source-foundry/font-unicode/master/lib/fontunicode/glyphlist/aglfn.txt>`__
to other executables with the ``list`` command:

::

    $ font-unicode list agl | [other executable]

The raw `Unicode Standard v8.0.0 names
list <https://raw.githubusercontent.com/source-foundry/font-unicode/master/lib/fontunicode/glyphlist/NamesList.txt>`__
can be piped to other executables with the ``list`` command:

::

    $ font-unicode list unicode | [other executable]

For example, you could use ``grep`` to locate a Unicode code point in
the semicolon delimited Adobe Glyph List like this:

::

    $ font-unicode list agl | grep '012E'
    012E;Iogonek;LATIN CAPITAL LETTER I WITH OGONEK

Licenses
--------

font-unicode is licensed under the MIT license. The full text of the
license is available
`here <https://github.com/source-foundry/font-unicode/blob/master/docs/LICENSE>`__.

The Adobe Glyph List for New Fonts is licensed under the Apache License,
v2.0. The full text of the license is available
`here <http://www.apache.org/licenses/LICENSE-2.0.html>`__.

The Unicode Standard v8.0.0 names list data file is licensed under the
Unicode License Agreement for Data Files and Software. The full text of
the license is available
`here <http://www.unicode.org/copyright.html>`__.
