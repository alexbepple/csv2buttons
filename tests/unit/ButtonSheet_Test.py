#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import *
#from mock import Mock, sentinel
from mockito import *
from reportlab.platypus import Paragraph
from reportlab.lib import styles
from ibp.buttonsheet import ButtonSheet

class ButtonSheet_with_a_template_and_an_element_factory_Test:

    @istest
    def printsOneButton(self):
        template = Mock()
        dummyFlowable = Mock()
        flowable_factory = Mock()
        
        button_text = "Peter Graf"
        
        sheet = ButtonSheet()
        sheet.add_button(button_text)
        
        when(flowable_factory).createParagraph(button_text).thenReturn(dummyFlowable)
        story = [dummyFlowable]
        
        sheet.build(template, flowable_factory)
        verify(template).build(story)

