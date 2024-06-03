# this is a simple code to extract text from a pdf file. It uses PyPDF2 to execute the process.

from PyPDF2 import PdfReader

reader = PdfReader ("MA-102 Teaching Plan.pdf")

str = ""
for i in range(3) :
    page = reader.pages[i]

    str = str + page.extract_text()



with open("text.txt" , "w" , encoding='utf-8') as f:
    f.write(str)