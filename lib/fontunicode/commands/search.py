#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3
from Naked.toolshed.system import stderr, stdout

# class UnicodeObject(object):
#     def __init__(self, adobe_glyphtext, unicode_glyphtext):
#         self.adobe_glyphtext = adobe_glyphtext
#         self.unicode_glyphtext = unicode_glyphtext
#         self.unicode_list = []
#         self.shortname_list = []
#         self.longname_list = []
#         self.unicode_shortname_map = {}
#         self.unicode_longname_map = {}
#         self._instantiate_unicode_object()  # load data
#
#     def _instantiate_unicode_object(self):
#         # Adobe Glyph List
#         m = re.compile(r"^(?P<unicode>[\dABCDEF]{4});(?P<shortname>\w*?);(?P<longname>[\w\-\s]*?)$", re.MULTILINE)
#         iterator = m.finditer(self.adobe_glyphtext)
#         for match in iterator:
#             unicode_position = match.group('unicode')
#             shortname = match.group('shortname')
#             longname = match.group('longname')
#             self.unicode_list.append(unicode_position)
#             self.shortname_list.append(shortname)
#             self.longname_list.append(longname)
#             self.unicode_shortname_map.update({unicode_position: shortname})
#             self.unicode_longname_map.update({unicode_position: longname})
#
#         # Unicode Name List
#         m2 = re.compile(r"^(?P<unicode>[\dABCDEF]*?)\t(?P<longname>[\w\-\s]*?)$", re.MULTILINE)
#         iterator2 = m2.finditer(self.unicode_glyphtext)
#         for match2 in iterator2:
#             unicode_position_uni = match2.group('unicode')
#             longname_uni = match2.group('longname')
#             if unicode_position_uni in self.unicode_list:
#                 # update the dictionary maps with unicode definiton of the long names (overwrite Adobe defintion)
#                 self.unicode_longname_map[unicode_position_uni] = longname_uni
#             else:
#                 self.unicode_list.append(unicode_position_uni)
#                 self.longname_list.append(longname_uni)
#                 self.unicode_shortname_map[unicode_position_uni] = ""  # empty string since there is no shortname
#                 self.unicode_longname_map[unicode_position_uni] = longname_uni  # define longname from Unicode data
#
#         # define a unicode set to use for tests of inclusion during searches
#         self.unicode_set = set(self.unicode_list)
#         self.shortname_set = set(self.shortname_list)
#         self.longname_set = set(self.longname_list)


def unicode_find(needle_list):
    con = None
    try:
        parent_directory = os.path.split(os.path.dirname(__file__))[0]
        db_filepath = os.path.join(parent_directory, "glyphlist", "unicode.db")
        con = sqlite3.connect(db_filepath, isolation_level=None)
        cur = con.cursor()

        for needle in needle_list:
            cur.execute("SELECT unicode, unishortname, unilongname FROM Unicodes WHERE unicode LIKE ?", (needle,))
            result = cur.fetchone()
            if result is not None:
                if len(result[1]) > 0:
                    result_string = result[0] + "\t" + result[1] + " '" + result[2] + "'"
                else:
                    result_string = result[0] + "\t'" + result[2] + "'"
                stdout(result_string)
            else:
                stderr(needle + "\t" + "NOT FOUND")
    except Exception as e:
        stderr("[font-unicode]: Error: " + str(e), exit=1)
    finally:
        if con:
            con.close()


def name_find(name_list):
    con = None
    try:
        parent_directory = os.path.split(os.path.dirname(__file__))[0]
        db_filepath = os.path.join(parent_directory, "glyphlist", "unicode.db")
        con = sqlite3.connect(db_filepath, isolation_level=None)
        cur = con.cursor()

        for needle in name_list:
            modified_needle = "%" + needle + "%"
            cur.execute("SELECT unicode, unishortname, unilongname FROM Unicodes WHERE unilongname LIKE ?", (modified_needle,))
            result_list = cur.fetchall()

            if len(result_list) > 0:
                for result in result_list:
                    stdout("'" + needle + "' ==> " + result[0] + " '" + result[2] + "'")
            else:
                stderr("[X] " + needle)
    except Exception as e:
        stderr("[font-unicode] Error: " + str(e), exit=1)
    finally:
        if con:
            con.close()
