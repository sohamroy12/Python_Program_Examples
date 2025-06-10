from fpdf import FPDF
from pathlib import Path
import glob

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

filePaths = glob.glob(f"Text+Files/*.txt")

for files in filePaths:
    with open(files) as f:
        text = f.read()
    pdf.add_page()
    fileName = Path(files).stem
    name = fileName.title()
        
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{name}", ln=1)
    pdf.set_font(family="Times", size=11)
    pdf.multi_cell(w=0, h=8, txt=text)
    
pdf.output(f"PDFs/All.pdf")