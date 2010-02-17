#!/usr/bin/env python
#-*- coding:utf-8 -*-

class ButtonSheet:

    button_texts = []

    def add_button(self, text):
        self.button_texts.append(text)
        return self
    
    def add_buttons(self, texts):
        for text in texts:
            self.add_button(text)
        return self

    def build(self, template, flowable_factory):
        paras = [flowable_factory.create_paragraph(text) for text in self.button_texts]
        separators = [flowable_factory.create_separator()] * len(paras)
        
        intertwined = sum([[x, y] for x, y, in zip(paras, separators)], [])
        story = intertwined[:-1]
        
        template.build(story)

