import PyPDF2

save_dir = "output"
# creating a pdf file object
pdfFile = open('file_1.pdf', 'rb')

# Creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFile)

# Printing number of pages in pdf file
print(len(pdfReader.pages))

# Generate a .txt file
file = open(save_dir + "/" + "extracted.txt", "w+")
file.write("")
file.close()

# Creating a page object
pageObj = pdfReader.pages[0]

# Extracting text from page
text = pageObj.extract_text()
print(text)

# Save as .txt file
file = open(save_dir + "/" + "extracted.txt", "a")
file.write(text)
file.close()

# closing the pdf file object
pdfFile.close()
