from pdfy import Pdfy

p = Pdfy(debug_port=9223)
p.html_to_pdf("https://www.aljazeera.net/", pdf_path="test.pdf")