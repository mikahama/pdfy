from pdfy import Pdfy

p = Pdfy(9223)
p.html_to_pdf("lasku_pohja.htm", pdf_path="lasku_pohja.pdf")