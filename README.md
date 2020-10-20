# Pdfy #

Pdfy is a Python library for converting HTML (and anything Chrome can render) into PDF. It uses Chrome printing functionality, so the PDFs will be rendered exactly as printed in the browser.

## Need for NLP solutions for your business?


<img src="https://rootroo.com/cropped-logo-01-png/" alt="Rootroo logo" width="128px" height="128px">

My company, [Rootroo offers consulting related to multilingual NLP tasks](https://rootroo.com/). We have a strong academic background in the state-of-the-art AI solutions for every NLP need. Just contact us, we won't bite.

## Installation ##

To install the library, you need to run.

    pip install pdfy

Additionally, [you will need to install Chrome Driver](http://chromedriver.chromium.org/getting-started). 

## Usage ##

Using the library is as easy as:

    from pdfy import Pdfy
    p = Pdfy()
    p.html_to_pdf("html_file.htm", pdf_path="pdf_file.pdf")

### More control over the PDF layout ###

If you need to have more control over the layout, you can pass additional parameters to html_to_pdf

    options = {"paperWidth": 8.3, "paperHeight":11.7}
    p.html_to_pdf("html_file.htm", pdf_path="pdf_file.pdf" options=options)

The full list of parameters is available on [Chrome's Developer site](https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-printToPDF).

### Not saving the PDF ###

In the absence of the pdf_path argument, the html_to_pdf function will return the PDF as a base64 encoded string.

    pdf = p.html_to_pdf("html_file.htm")


### Multiple instances ###

The library will run Chrome in the background in the remote debug mode. This means that if your project requires multiple initialized Pdfy objects, you might need to change the port used for debugging. This can be done by passing the port number to Pdfy() as follows:

    p = Pdfy(debug_port=9222) #9222 is the default port

## Credits ##

This library is released under [the Apache 2.0 License](https://opensource.org/licenses/Apache-2.0).

(C) Copyright 2018-2020 [Mika Hämäläinen](https://mikakalevi.com)

## Cite

	@software{mika_hamalainen_2020_4108770,
	  author       = {Mika Hämäläinen and
	                  Hiromu Hota and
	                  Mike and
	                  Mirza Delic},
	  title        = {mikahama/pdfy 1.0.50},
	  month        = oct,
	  year         = 2020,
	  publisher    = {Zenodo},
	  version      = {1.0.50},
	  doi          = {10.5281/zenodo.4108770},
	  url          = {https://doi.org/10.5281/zenodo.4108770}
	}
