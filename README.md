# Pdfy #

Pdfy is a Python library for converting HTML (and anything Chrome can render) into PDF. It uses Chrome printing functionality, so the PDFs will be rendered exactly as printed in the browser.

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

(C) Copyright 2018 [Mika Hämäläinen](https://mikakalevi.com)

## Cite

    @software{mika_hamalainen_2020_3977555,
      author       = {Mika Hämäläinen and
                      Mike and
                      Mirza Delic},
      title        = {mikahama/pdfy 1.0.40},
      month        = aug,
      year         = 2020,
      publisher    = {Zenodo},
     version      = {1.0.40},
      doi          = {10.5281/zenodo.3977555},
      url          = {https://doi.org/10.5281/zenodo.3977555}
    }
