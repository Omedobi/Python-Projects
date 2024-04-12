import PyPDF2


pdf = open("Text Extraction from PDF\data\EORTC404112-QLQ-HCC18-English.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
page = reader.pages[0]
text = page.extract_text()
print(text)
pdf.close()