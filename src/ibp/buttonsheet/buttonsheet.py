#!/usr/bin/env python
#-*- coding:utf-8 -*-

class ButtonSheet:

    def add_button(self, text):
        self.button_text = text

    def build(self, template, flowable_factory):
        paragraph = flowable_factory.createParagraph(self.button_text)
        template.build([paragraph])

