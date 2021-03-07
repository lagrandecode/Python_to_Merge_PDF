from PyPDF2 import PdfFileReader, PdfFileMerger
pdf_file1 = PdfFileReader(r"C:\Users\OLUWASEUN\Desktop\python_work\a.pdf")
pdf_file2 = PdfFileReader(r"C:\Users\OLUWASEUN\Desktop\python_work\b.pdf")
#create a pdf merger
output = PdfFileMerger()

output.append(pdf_file1)
output.append(pdf_file2)

output.write(r"C:\Users\OLUWASEUN\Desktop\python_work\merged2.pdf")