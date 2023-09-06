from PyPDF2 import Pdfwriter,PdfReader
num=int(input("enter page no you want to combine from multiple document"))
Pdf1=open('program.pdf','rb')
pdf2=open('aimlsyll.pdf','rb')
pdf_writer=Pdfwriter()
pdf_reader=PdfReader(Pdf1)
page=Pdf1_Reader.pages[num-1]
wpdf_writer.add_pages[page]
Pdf2_reader=PdfReader(pdf2)
page=pdf2.reader_pages[num-1]
pdf_writer.add_pages(page)
with open('output.pdf','wb')as output:
    pdf_writer.write(output)
