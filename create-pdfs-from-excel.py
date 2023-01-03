from fpdf import FPDF
import pandas as pd
import openpyxl

df = pd.read_excel('data.xlsx', )
print(df)
print(df.columns)
for index, row in df.iterrows():
    # build pdf, blah blah...
    print(row['name'])
