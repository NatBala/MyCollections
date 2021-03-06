from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, TextConverter, XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io


# setting absolute paths
prjPath = r'C:\Users\Natarajan\Desktop\PDFParser'


def convert(case, fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    manager = PDFResourceManager()
    codec = 'utf-8'
    caching = True

    if case == 'text':
        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
    if case == 'HTML':
        output = io.BytesIO()
        converter = HTMLConverter(manager, output, codec=codec, laparams=LAParams())

    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(fname, 'rb')

    for page in PDFPage.get_pages(infile, pagenums, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    convertedPDF = output.getvalue()

    infile.close()
    converter.close()
    output.close()
    return convertedPDF


paredPDF = convert('text', r'C:\Users\Natarajan\Desktop\PDFParser\SamplePDF.pdf')
print(paredPDF)

# export the parsed file to text file
with open(r'')
