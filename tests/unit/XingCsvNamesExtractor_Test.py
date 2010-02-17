#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import *
import xing

class XingCsvNamesExtractor_Test:
    
    @istest
    def extracts_names(self):
        names = xing.extract_names_from_csv("""
"Joanna"
"Gill Sans"
""")
        assert_equal(["Joanna", "Gill Sans"], names)

    @istest
    def ignores_all_columns_but_first__columns_are_tab_separated(self):
        names = xing.extract_names_from_csv("""
"Joanna"	"was"	"born"
""")
        assert_equal(["Joanna"], names)
    