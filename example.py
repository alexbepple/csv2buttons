from ibp.buttonsheet import ButtonSheet
from ibp.templates import TemplateFor55Buttons
from ibp.elements import FlowableFactory
import xing

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import codecs
from subprocess import call


pdfmetrics.registerFont(TTFont('default', 'GillSansBold.ttf'))

pdf_filename = "xing.pdf"
template = TemplateFor55Buttons(pdf_filename)

with codecs.open('xing.csv', encoding='utf-16-le') as f:
    lines = f.readlines()
lines = [line.encode('utf-8') for line in lines]

names = xing.extract_names_from_csv(lines)
ButtonSheet().add_buttons(names).build(template, FlowableFactory())

call(["xdg-open", pdf_filename])

