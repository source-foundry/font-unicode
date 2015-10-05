#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
# font-unicode
# Copyright 2015 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------


# Application start
def main():
    import os
    import sys
    from Naked.commandline import Command
    from Naked.toolshed.state import StateObject

    # ------------------------------------------------------------------------------------------
    # [ Instantiate command line object ]
    #   used for all subsequent conditional logic in the CLI application
    # ------------------------------------------------------------------------------------------
    c = Command(sys.argv[0], sys.argv[1:])
    # ------------------------------------------------------------------------------
    # [ Instantiate state object ]
    # ------------------------------------------------------------------------------
    state = StateObject()
    # ------------------------------------------------------------------------------------------
    # [ Command Suite Validation ] - early validation of appropriate command syntax
    # Test that user entered at least one argument to the executable, print usage if not
    # ------------------------------------------------------------------------------------------
    if not c.command_suite_validates():
        from fontunicode.settings import usage as fontunicode_usage
        print(fontunicode_usage)
        sys.exit(1)
    # ------------------------------------------------------------------------------------------
    # [ NAKED FRAMEWORK COMMANDS ]
    # Naked framework provides default help, usage, and version commands for all applications
    #   --> settings for user messages are assigned in the lib/fontunicode/settings.py file
    # ------------------------------------------------------------------------------------------
    if c.help():      # User requested fontunicode help information
        from fontunicode.settings import help as fontunicode_help
        print(fontunicode_help)
        sys.exit(0)
    elif c.usage():   # User requested fontunicode usage information
        from fontunicode.settings import usage as fontunicode_usage
        print(fontunicode_usage)
        sys.exit(0)
    elif c.version(): # User requested fontunicode version information
        from fontunicode.settings import app_name, major_version, minor_version, patch_version
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)
    # ------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    # ------------------------------------------------------------------------------------------

    if c.cmd == "print":
        text = open(os.path.join(os.path.dirname(__file__), 'glyphlist', 'aglfn.txt')).read()
        print(text)

    # ------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    #  Message to provide to the user when all above conditional logic fails to meet a true condition
    # ------------------------------------------------------------------------------------------
    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1) #exit

if __name__ == '__main__':
    main()