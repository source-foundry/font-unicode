#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import re
import os
import sys


class UnicodeObject(object):
    def __init__(self, adobe_glyphtext, unicode_glyphtext):
        self.adobe_glyphtext = adobe_glyphtext
        self.unicode_glyphtext = unicode_glyphtext
        self.unicode_list = []
        self.shortname_list = []
        self.longname_list = []
        self.unicode_shortname_map = {}
        self.unicode_longname_map = {}
        self._instantiate_unicode_object()  # load data

    def _instantiate_unicode_object(self):
        # Adobe Glyph List
        m = re.compile(r"^(?P<unicode>[\dABCDEF]{4});(?P<shortname>\w*?);(?P<longname>[\w\-\s]*?)$", re.MULTILINE)
        iterator = m.finditer(self.adobe_glyphtext)
        for match in iterator:
            unicode_position = match.group('unicode')
            shortname = match.group('shortname')
            longname = match.group('longname')
            self.unicode_list.append(unicode_position)
            self.shortname_list.append(shortname)
            self.longname_list.append(longname)
            self.unicode_shortname_map.update({unicode_position: shortname})
            self.unicode_longname_map.update({unicode_position: longname})

        # Unicode Name List
        m2 = re.compile(r"^(?P<unicode>[\dABCDEF]*?)\t(?P<longname>[\w\-\s]*?)$", re.MULTILINE)
        iterator2 = m2.finditer(self.unicode_glyphtext)
        for match2 in iterator2:
            unicode_position_uni = match2.group('unicode')
            longname_uni = match2.group('longname')
            if unicode_position_uni in self.unicode_list:
                # update the dictionary maps with unicode definiton of the long names (overwrite Adobe defintion)
                self.unicode_longname_map[unicode_position_uni] = longname_uni
            else:
                self.unicode_list.append(unicode_position_uni)
                self.longname_list.append(longname_uni)
                self.unicode_shortname_map[unicode_position_uni] = ""  # empty string since there is no shortname
                self.unicode_longname_map[unicode_position_uni] = longname_uni  # define longname from Unicode data


# START DATA GENERATOR, CREATE DB TABLE

adobeglyphlist_text = open(os.path.join(os.path.dirname(__file__), 'aglfn.txt')).read()
unicodeglyphlist_text = open(os.path.join(os.path.dirname(__file__), 'NamesList.txt')).read()

uniobj = UnicodeObject(adobeglyphlist_text, unicodeglyphlist_text)

con = None

try:
    con = sqlite3.connect("unicode.db", isolation_level=None)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Unicodes")
        cur.execute("CREATE TABLE Unicodes (id INT PRIMARY KEY, unicode TEXT, unishortname TEXT, unilongname TEXT)")

        key = 1
        unicodes = []
        for unicode_position in uniobj.unicode_list:
            this_tuple = (key, unicode_position, uniobj.unicode_shortname_map[unicode_position], uniobj.unicode_longname_map[unicode_position])
            unicodes.append(this_tuple)
            key += 1

        unicodes_tuple = tuple(unicodes)
        cur.executemany("INSERT INTO Unicodes VALUES(?, ?, ?, ?)", unicodes_tuple)

except Exception as e:
    if con:
        con.rollback()
    sys.stderr.write("ERROR: " + str(e))
    sys.exit(1)
finally:
    if con:
        con.close()

