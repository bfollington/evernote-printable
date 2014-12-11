evernote-printable
==================

Evernote sucks at printing, since it can't display embedded PDF's.

This is a python script that converts an HTML exported evernote note (or many) into a pdf with embedded pdf fragments. It converts all embedded pdfs to pngs, reformats the HTML files to include them, resizes images in the HTML file and then converts the HTML to a pdf.

It depends on `ghostscript`, `imagemagick` and `wkhtmltopdf` to do the actual conversion. It will operate on all exported HTML notes in the current directory when it is run.
