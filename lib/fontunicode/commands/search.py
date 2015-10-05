#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


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

        # define a unicode set to use for tests of inclusion during searches
        self.unicode_set = set(self.unicode_list)
        self.shortname_set = set(self.shortname_list)
        self.longname_set = set(self.longname_list)


class UnicodeSearcher(object):
    def __init__(self, unicode_object):
        self.unicode_object = unicode_object

    def find(self, needle):
        if needle in self.unicode_object.unicode_set:
            print(needle + "\t" + self.unicode_object.unicode_shortname_map[needle] + " '" + self.unicode_object.unicode_longname_map[needle] + "'")
        else:
            if len(needle) > 5 or len(needle) < 4:  # should be 4 numbers in length
                print(needle + "\t" + "ERROR: Bad Unicode search string")
            else:
                print(needle + "\t" + "UNICODE POSITION NOT FOUND")


class NameSearcher(object):
    def __init__(self, data, unicode_object):
        pass

