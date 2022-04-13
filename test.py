from pdfy import Pdfy

p = Pdfy()
p.html_to_pdf("https://www.rootroo.com/", pdf_path="test.pdf")