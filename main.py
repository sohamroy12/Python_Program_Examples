from tkinter.ttk import Style

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="a4")
df = pd.read_csv("./topics.csv")

for item, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=22)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, txt=row["Topic"], h=12, align="L", ln=1)
    pdf.line(10, 27, 200, 27)

pdf.output("output.pdf")


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
