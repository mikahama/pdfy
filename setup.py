#encoding: utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfy",
    version="1.0.10",
    author="Mika Hämäläinen",
    author_email="mika.hamalainen@helsinki.fi",
    description="A library for converting HTML files into PDF. The tool uses Chrome to render the HTML and print it into a pdf file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikahama/pdfy",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
    ),
)