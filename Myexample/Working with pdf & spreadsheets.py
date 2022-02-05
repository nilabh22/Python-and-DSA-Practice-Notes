import csv
file = open('C:\\Users\\Nilabh Sahu\\PycharmProjects\\Myexample\\example\\example.csv',encoding='utf-8')
csv_data = csv.reader(file)
data_lines = list(csv_data)
print(data_lines)

# 2 - a).Working with PDF's

import PyPDF2
f = open('C:\\Users\\Nilabh Sahu\\PycharmProjects\\Myexample\\Working_Business_Proposal\\Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages) # Print the number of pages in the pdf file
page_one = pdf_reader.getPage(0) # 0 is the index position of the page we wanted to grab
page_one_text = page_one.extractText()
print(page_one_text)
f.close()

# b) Writing to a pdf file
f = open('C:\\Users\\Nilabh Sahu\\PycharmProjects\\Myexample\\Working_Business_Proposal\\Working_Business_Proposal.pdf','rb')
pdf_reader =PyPDF2.PdfFileReader(f)
page_one =pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
add_page = pdf_writer.addPage(page_one)
pdf_output = open('C:\\Users\\Nilabh Sahu\\PycharmProjects\\Myexample\\Some_BrandNew_Doc\\Some_BrandNew_Doc.pdf','wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

