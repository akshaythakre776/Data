import PyPDF2
pdfObj = open('C://Users//athakre//Desktop//Python//Python_New//files//image.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)
# print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
pdfObj.close()