# PyJPDF

PyJPDF is a Python library for extracting information from PDF files.

## Author

Jasson Carvalho

## Version

0.1.3

## Installation

```bash
pip install pyjpdf
```

## Usage

```bash
import pyjpdf as PyJPDF

p = PyJPDF.PyjPDFExtract()

## From URL
text = p.from_url('http://www.example.com/teste.pdf')

## From File
text = p.from_file('teste.pdf')

## From Stream
text = p.from_stream(open('teste.pdf', 'rb'))
```
