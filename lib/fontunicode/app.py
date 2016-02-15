#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# font-unicode
# Copyright 2016 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------


# Application start
def main():
    import os
    import sys
    from commandlines import Command
    from fontunicode.commands.search import name_find, unicode_find

    c = Command()

    if c.does_not_validate_missing_args():
        from fontunicode.settings import usage as fontunicode_usage
        print(fontunicode_usage)
        sys.exit(1)

    if c.is_help_request():      # User requested fontunicode help information
        from fontunicode.settings import help as fontunicode_help
        print(fontunicode_help)
        sys.exit(0)
    elif c.is_usage_request():   # User requested fontunicode usage information
        from fontunicode.settings import usage as fontunicode_usage
        print(fontunicode_usage)
        sys.exit(0)
    elif c.is_version_request():  # User requested fontunicode version information
        from fontunicode.settings import app_name, major_version, minor_version, patch_version
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)

    # ------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    # ------------------------------------------------------------------------------------------

    if c.subcmd == "list":
        if c.subsubcmd == "agl":
            adobeglyphlist_text = open(os.path.join(os.path.dirname(__file__), 'glyphlist', 'aglfn.txt')).read()
            print(adobeglyphlist_text)
            sys.exit(0)
        elif c.subsubcmd == "unicode":
            unicodenamelist_text = open(os.path.join(os.path.dirname(__file__), 'glyphlist', 'NamesList.txt')).read()
            print(unicodenamelist_text)
            sys.exit(0)
    elif c.subcmd == "search":
        # if there is not a search, term raise error message and exit
        if c.argc == 1:
            sys.stderr.write("[font-unicode]: Error: Please enter a Unicode search term.\n")
            sys.exit(1)

        search_list = c.argv[1:]  # include all command line arguments after the primary command
        unicode_search_list = []

        for needle in search_list:
            if needle.startswith('u+') or needle.startswith('U+'):
                unicode_search_list.append(needle[2:])  # remove the u+ before adding it to the list for search
            else:
                unicode_search_list.append(needle)

        if len(unicode_search_list) > 0:
            unicode_find(unicode_search_list)
    elif c.subcmd == "name":
        # if there is not a search, term raise error message and exit
        if c.argc == 1:
            sys.stderr.write("[font-unicode]: Error: Please enter a glyph name search term.\n")

        search_list = c.argv[1:]
        name_search_list = []

        for needle in search_list:
            name_search_list.append(needle)

        if len(name_search_list) > 0:
            name_find(name_search_list)
    # ------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    #  Message to provide to the user when all above conditional logic fails to meet a true condition
    # ------------------------------------------------------------------------------------------
    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1)  # exit

if __name__ == '__main__':
    main()
