from docx import Document

doc = Document('cv-jtv.docx')

for para in doc.paragraphs:
    print(para.text)