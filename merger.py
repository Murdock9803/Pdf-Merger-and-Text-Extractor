# this is a simple code to merge many pdf files to one. it uses PyPDF2 to execute the task.

from PyPDF2 import PdfMerger

#write names of pdf files in the list below in place of one.pdf and two.pdf
pdfs = ["one.pdf" , "two.pdf"]

merger = PdfMerger()

for pdf in pdfs : 
    merger.append(pdf)


# write the name of your desired merged pdf in place of merged.pdf below
merger.write("merged.pdf")
merger.close()
