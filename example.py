from ibp.buttonsheet import ButtonSheet
from ibp.templates import TemplateFor55Buttons
from ibp.elements import FlowableFactory

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('GillSans-Bold', 'GillSansBold.ttf'))

pdf_filename = "example.pdf"
template = TemplateFor55Buttons(pdf_filename)

#with open('example.csv')

import xing
names = xing.extract_names_from_csv("""
xing_name	last_name	first_name
"Gill Sans"	"Gill"	"Sans"
"Joanna"	""	""
"Myriad"	""	""
"Calibri"	""	""
"Consolas"	""	""
"Bookman Old Style"	"Bookman"	"Old Style"
"Scala"	""	""
""")

ButtonSheet().add_buttons(names).build(template, FlowableFactory())

from subprocess import call
call(["xdg-open", pdf_filename])

