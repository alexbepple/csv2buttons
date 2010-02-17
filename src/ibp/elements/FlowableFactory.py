#!/usr/bin/env python
#-*- coding:utf-8 -*-


from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import *

class FlowableFactory:
    
    def createParagraph(self, text):
        return Paragraph(text, self.createStyle())
    
    def createStyle(self):
        return ParagraphStyle("Normal", alignment = TA_CENTER, fontName='GillSans-Bold', fontSize=18)
