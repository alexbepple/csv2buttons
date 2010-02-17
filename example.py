from ibp.buttonsheet import ButtonSheet
from ibp.templates import TemplateFor55Buttons
from ibp.elements import FlowableFactory
import xing

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('GillSans-Bold', 'GillSansBold.ttf'))

pdf_filename = "example.pdf"
template = TemplateFor55Buttons(pdf_filename)

with open('example.csv', 'r') as f:
    csv_contents = f.readlines() 
names = xing.extract_names_from_csv(csv_contents)

ButtonSheet().add_buttons(names).build(template, FlowableFactory())

from subprocess import call
call(["xdg-open", pdf_filename])

