#!/usr/bin/env python
#-*- coding:utf-8 -*-

from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib.units import mm

class TemplateFor55Buttons:

    def __init__(self, filename):
        self.template = BaseDocTemplate(filename)
        # this actually creates 68 mm. Why?         
        size = 78 * mm
        frame = Frame(30, 400, size, size, topPadding = size / 2 - 10, showBoundary=True)
        page_template = PageTemplate(frames=[frame])
        self.template.addPageTemplates(page_template)
        
    def build(self, story):
        self.template.build(story)

