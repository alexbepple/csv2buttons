#!/usr/bin/env python
#-*- coding:utf-8 -*-

from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib.units import mm


class TemplateFor55Buttons(BaseDocTemplate):

    def __init__(self, filename):
        BaseDocTemplate.__init__(self, filename)
        self.button_renderer = ButtonRenderer()
        
        page_template = PageTemplate(frames=self._create_frames())
        self.addPageTemplates(page_template)
        
    def handle_frameBegin(self, resume = 0):
        self.button_renderer.render_button(self.frame, self.canv)
        self._handle_frameBegin()
        
    def _create_frames(self, frames=[]):
        x_positions = [70, 300]
        y_positions = [20, 300, 600]
        for x in x_positions:
            frames.extend([self.button_renderer.create_frame(x, y) for y in y_positions])
        return frames
    

class ButtonRenderer:
    outer_size = 68*mm
    inner_size = 55*mm
    
    def create_frame(self, x, y):
        return Frame(x, y, self.outer_size, self.outer_size, topPadding = self.outer_size / 2 - 10, showBoundary=True)

    def render_button(self, frame, canvas):
        self.render_logo(frame, canvas)
        self.render_inner_circle(frame, canvas)
    
    def render_logo(self, frame, canvas):
        width = self.inner_size - 40
        left_offset = 40
        top_offset = 80
        canvas.drawImage("logo.png", frame.x1+left_offset, frame.y1+self.outer_size-top_offset, width=width, preserveAspectRatio=True)

    def render_inner_circle(self, frame, canvas):
        canvas.circle(frame.x1 + self.outer_size / 2, frame.y1 + self.outer_size /2, self.inner_size / 2 + 5)

