import PyPDF2


pdf = open("Text Extraction from PDF\data\EORTC404112-QLQ-HCC18-English.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)

for page_no, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"Page {page_no + 1}:\n{text}\n")
    
pdf.close()