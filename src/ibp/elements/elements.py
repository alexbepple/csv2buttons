
from reportlab.platypus import Paragraph, doctemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import *

class FlowableFactory:
    
    def create_paragraph(self, text):
        return Paragraph(text, self.createStyle())
    
    def create_separator(self):
        return doctemplate.FrameBreak
    
    def createStyle(self):
        return ParagraphStyle("Normal", alignment = TA_CENTER, fontName='GillSans-Bold', fontSize=18)
