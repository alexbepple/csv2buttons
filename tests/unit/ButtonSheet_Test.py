#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import *
#from mock import Mock, sentinel
from mockito import *
from reportlab.platypus import Paragraph
from reportlab.lib import styles
from ibp.buttonsheet import ButtonSheet

class ButtonSheet_with_a_template_and_an_element_factory_Test:

    def setUp(self):
        self.sheet = ButtonSheet()
        self.template = Mock()
        self.sentinel_paragraph = Mock()
        self.sentinel_separator = Mock()
        self.element_factory = Mock()
        self.text1 = "Peter Graf" 

    @istest
    def printsOneButton(self):
        self.sheet.add_button(self.text1)
        when(self.element_factory).create_paragraph(self.text1).thenReturn(self.sentinel_paragraph)
        
        self.sheet.build(self.template, self.element_factory)
        
        story = [self.sentinel_paragraph]
        verify(self.template).build(story)

    @istest
    def separates_two_buttons_with_an_indicator(self):
        self.sheet.add_button(self.text1)
        when(self.element_factory).create_paragraph(self.text1).thenReturn(self.sentinel_paragraph)
        when(self.element_factory).create_separator().thenReturn(self.sentinel_separator)
        
        self.sheet.build(self.template, self.element_factory)
        
        story = [self.sentinel_paragraph, self.sentinel_separator, self.sentinel_paragraph]
        verify(self.template).build(story)

