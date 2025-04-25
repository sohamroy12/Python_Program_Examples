import PyPDF2

reader = PyPDF2.PdfReader("twopage.pdf")
meta = reader.metadata

print(len(reader.pages))
# All of the following could be None!
# print(meta.author)
# print(meta.creator)
# print(meta.producer)
# print(meta.subject)
# print(meta.title)


page = reader.pages[1]
# print(page.extract_text())
# extract only text oriented up
print(page.extract_text(0))
# extract text oriented up and turned left
print(page.extract_text((0, 180)))


template = PyPDF2.PdfReader(open('super.pdf', 'rb')) # rb is read binary
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))  # rb is read binary
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('watermaked_output.pdf', 'wb') as outputFile:
    output.write(outputFile)
