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

sheet = ButtonSheet()
sheet.add_button("Gill Sans")
sheet.add_button("Joanna")
sheet.add_button("Myriad")
sheet.add_button("Calibri")
sheet.add_button("Consolas")
sheet.add_button("Bookman Old Style")
sheet.add_button("Scala")
sheet.build(template, FlowableFactory())

from subprocess import call
call(["xdg-open", pdf_filename])

