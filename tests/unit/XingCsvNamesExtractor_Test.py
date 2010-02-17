#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import *
import xing

class XingCsvNamesExtractor_Test:
    
    @istest
    def cleans_up_names(self):
        names = xing.extract_names_from_csv(['"Joanna"'])
        assert_equal(["Joanna"], names)
    
    @istest
    def ignores_empty_lines(self):
        names = xing.extract_names_from_csv([''])
        assert_equal([], names)

    @istest
    def ignores_all_columns_but_first__columns_are_tab_separated(self):
        names = xing.extract_names_from_csv(['"Joanna"	"was"	"born"'])
        assert_equal(["Joanna"], names)

    @istest
    def ignores_header_which_is_discernible_by_lack_of_quotation(self):
        names = xing.extract_names_from_csv(['name', '"Joanna"'])
        assert_equal(["Joanna"], names)

