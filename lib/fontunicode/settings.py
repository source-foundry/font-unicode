#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
# Application Name
# ------------------------------------------------------------------------------
app_name = 'font-unicode'

# ------------------------------------------------------------------------------
# Version Number
# ------------------------------------------------------------------------------
major_version = "0"
minor_version = "9"
patch_version = "1"

# ------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
# ------------------------------------------------------------------------------
debug = False

# ------------------------------------------------------------------------------
# Usage String
# ------------------------------------------------------------------------------
usage = """
font-unicode [primary cmd] [arg 1] <arg 2> <...arg x>

Primary Commands: list, name, search
Use `font-unicode --help` for more information
"""

# ------------------------------------------------------------------------------
# Help String
# ------------------------------------------------------------------------------
help = """---------------------------------------------------------
 font-unicode
 Unicode character code point and character name search
 Copyright 2015 Christopher Simpkins
 MIT license
 Source: https://github.com/source-foundry/font-unicode
---------------------------------------------------------

ABOUT

font-unicode is a command line search tool for identification of Unicode character name by code point search, and code point by name search.

It supports the Unicode Standard v8.0 and data are supplemented with the Adobe Glyph List for New Fonts v1.7 glyph names where applicable.

PRIMARY COMMANDS

  list: pipe raw Unicode standard data to standard output
  name: search by Unicode character name
search: search by Unicode code point

USAGE

  Search by Unicode Code Point
   $ font-unicode search [code point 1] <...code point X>

  Search by Unicode Character Name
   $ font-unicode name [name query 1] <...name query X>

  Pipe Raw Adobe Glyph List Data to Another Executable
   $ font-unicode list agl | [other executable]

  Pipe Raw Unicode Standard Data to Another Executable
   $ font-unicode list unicode | [other executable]"""