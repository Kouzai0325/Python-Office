from docx import Document

document = Document()

document.add_heading('ezpg', 0)
document.add_paragraph('csgo')

document.add_picture("a.png")

for para in docx.paragraphs:
        num = num + 1
        print(num, para.text)
print(len(num))

document.save('sample.docx')