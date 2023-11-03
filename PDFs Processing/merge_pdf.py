import PyPDF2
import sys
import os

# Create a merge object
merger = PyPDF2.PdfFileMerger(strict=False)

# Output folder
save_dir = "output"

# Merge pdf files
for file in os.listdir(os.curdir):
	if file.endswith(".pdf"):
		merger.append(file)

merger.write(save_dir + "/" + "merged_file.pdf")
merger.close()
