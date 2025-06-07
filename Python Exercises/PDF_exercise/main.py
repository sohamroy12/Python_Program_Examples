from fpdf import FPDF
from pathlib import Path
import glob

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

filePaths = glob.glob(f"Text+Files/*.txt")

for files in filePaths:
    pdf.add_page()
    fileName = Path(files).stem
    name = fileName.title()
        
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{name}")
    
pdf.output(f"PDFs/All.pdf")