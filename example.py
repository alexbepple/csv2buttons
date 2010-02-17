from reportlab.pdfgen.canvas import Canvas

#pdf = Canvas("test.pdf")
#pdf.drawImage("logo.jpg", 20, 500, width=100, preserveAspectRatio=True)
#pdf.showPage()
#pdf.save()


from ibp.buttonsheet import ButtonSheet
from ibp.templates import TemplateFor55Buttons
from ibp.elements import FlowableFactory

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('GillSans-Bold', 'GillSansBold.ttf'))

pdf_filename = "example.pdf"
template = TemplateFor55Buttons(pdf_filename)

import xing
names = xing.extract_names_from_csv("""
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

