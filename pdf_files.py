import PyPDF2
import os

os.chdir('/mnt/c/Users/ckgallow/Downloads')

pdfFile = open('meetingminutes.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

# print(reader.numPages)
# page = reader.getPage(0)
# print(page.extractText())
# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    writer.addPage(page)
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)

outputFile.close()
pdfFile.close()
pdfFile2.close()
