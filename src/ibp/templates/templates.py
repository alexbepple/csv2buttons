#!/usr/bin/env python
#-*- coding:utf-8 -*-

from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib.units import mm

class TemplateFor55Buttons:

    def __init__(self, filename):
        self.template = BaseDocTemplate(filename)
        page_template = PageTemplate(frames=self._createFrames())
        self.template.addPageTemplates(page_template)
        
    def build(self, story):
        self.template.build(story)

    def _createFrames(self, frames=[]):
        # This actually creates 68 mm. Why?         
        size = 78 * mm
        x_positions = [70, 300]
        y_positions = [20, 300, 600]
        for x in x_positions:
            frames.extend([self._createFrame(x, y, size) for y in y_positions])
        return frames
    
    def _createFrame(self, x, y, size):
        return Frame(x, y, size, size, topPadding = size / 2 - 10, showBoundary=True)
