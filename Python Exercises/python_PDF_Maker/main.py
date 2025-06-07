from tkinter.ttk import Style

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("./topics.csv")

for item, row in df.iterrows():
    pdf.add_page()

    # Set Header
    pdf.set_font(family="Times", style="B", size=22)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, txt=row["Topic"], h=12, align="L", ln=1)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Set Footer
    pdf.ln(254)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, txt=row["Topic"], h=12, align="R")

    for i in range(row["Pages"] -1):
        pdf.add_page()
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # Set Header
        # pdf.set_font(family="Times", style="B", size=22)
        # pdf.set_text_color(0, 0, 0)
        # pdf.cell(w=0, txt=row["Topic"], h=12, align="L", ln=1)
        # pdf.line(10, 20, 200, 20)

        # Set Footer
        pdf.ln(268)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, txt=row["Topic"], h=12, align="R")

pdf.output("output.pdf")


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
